# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import ast
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TLSPolicyTests(unittest.TestCase):
    def test_manifest_requires_a_new_explicit_opt_out(self):
        manifest = json.loads((ROOT / "watsonv3.json").read_text())
        configuration = manifest["configuration"]

        self.assertNotIn("verify_server_cert", configuration)
        self.assertFalse(configuration["allow_insecure_tls"]["default"])

    def test_requests_verify_unless_new_opt_out_is_enabled(self):
        source = (ROOT / "watsonv3_connector.py").read_text()
        tree = ast.parse(source)
        handler = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == "_make_rest_call")
        handler_source = ast.get_source_segment(source, handler)

        self.assertIn("not bool(config.get(consts.WATSONV3_JSON_ALLOW_INSECURE_TLS, False))", handler_source)
        self.assertIn("verify=verify_server_cert", handler_source)
        self.assertNotIn("WATSONV3_JSON_VERIFY_SERVER_CERT", handler_source)


if __name__ == "__main__":
    unittest.main()
