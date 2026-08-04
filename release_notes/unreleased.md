**Unreleased**

* Replaced the legacy certificate-verification field with an explicit insecure-TLS opt-out that defaults to disabled.
* Existing assets that intentionally require unverified TLS must enable the new opt-out after upgrade; legacy saved false values are not inherited.
