[comment]: # "Auto-generated SOAR connector documentation"
# Watson - Language Translator V3

Publisher: Splunk  
Connector Version: 1.0.4  
Product Vendor: IBM  
Product Name: Watson Language Translator V3  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.1.0  

Leverage IBM Watson for language translation using API version V3

[comment]: # " File: README.md"
[comment]: # "  Copyright (c) 2021-2023 Splunk Inc."
[comment]: # "  Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
Before you begin using the app:

-   Go to the Watson Developer Console
    [Services](https://console.ng.bluemix.net/developer/watson/services) page.
-   Select Language Translator, click Add Services, and either sign up for a free IBM Cloud account
    or log in.
-   Give a name to the project for example **PhantomLanguageApp** and click Create Project.
-   Copy the credentials (api key, url and current api version) to authenticate to the App Asset
    Config.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Watson Language Translator V3 asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** |  required  | string | Watson URL
**verify_server_cert** |  optional  | boolean | Verify server certificate
**api_key** |  required  | password | Watson API key
**version** |  optional  | string | Watson current API version (YYYY-MM-DD)

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[get language](#action-get-language) - Identifies the language of a given body of text  
[list languages](#action-list-languages) - List languages that can be used for translation  
[list translations](#action-list-translations) - List languages translation models  
[translate text](#action-translate-text) - Translate text from one language to another  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get language'
Identifies the language of a given body of text

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**text** |  required  | Text to identify | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.text | string |  |   Il s'agit d'un nouveau test  Bonjour comment allez-vous 
action_result.data.\*.confidence | numeric |  |   0.836794 
action_result.data.\*.language | string |  `language`  |   fr 
action_result.data.\*.languages.\*.confidence | numeric |  |   0.995919 
action_result.data.\*.languages.\*.language | string |  |   fr 
action_result.summary.high_confidence_match | string |  `language`  |   fr 
action_result.summary.total_languages | numeric |  |   62 
action_result.message | string |  |   High confidence match: fr, Total languages: 62 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list languages'
List languages that can be used for translation

Type: **generic**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.data.\*.language | string |  `language`  |   fr 
action_result.data.\*.name | string |  |   French 
action_result.summary.total_languages | numeric |  |   62 
action_result.message | string |  |   Total languages: 62 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list translations'
List languages translation models

Type: **generic**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.data.\*.base_model_id | string |  |  
action_result.data.\*.customizable | boolean |  |   True  False 
action_result.data.\*.default_model | boolean |  |   True  False 
action_result.data.\*.domain | string |  `domain`  |   conversational 
action_result.data.\*.model_id | string |  `watson translation model`  |   en-fr 
action_result.data.\*.name | string |  |   en-es-conversational 
action_result.data.\*.owner | string |  |  
action_result.data.\*.source | string |  |   en 
action_result.data.\*.status | string |  |   available 
action_result.data.\*.target | string |  |   es 
action_result.data.\*.training_log | string |  |  
action_result.summary.total_models | numeric |  |   32 
action_result.message | string |  |   Total models: 32 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'translate text'
Translate text from one language to another

Type: **generic**  
Read only: **True**

If model_id is specified the source and target parameters are ignored.<br>If the action fails with the error <i>Model not found</i>, it means the service cannot translate the text as is and a customized model needs to be created. Please see the Watson Language Translator documentation for instructions on creating a customized model.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**text** |  required  | Text to translate | string | 
**source** |  optional  | Source language | string |  `language` 
**target** |  optional  | Target language | string |  `language` 
**model_id** |  optional  | Translation Model | string |  `watson translation model` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.model_id | string |  `watson translation model`  |   en-fr 
action_result.parameter.source | string |  `language`  |   en 
action_result.parameter.target | string |  `language`  |   fr 
action_result.parameter.text | string |  |   this is a test again 
action_result.data.\*.character_count | numeric |  |   20 
action_result.data.\*.translations.\*.translation | string |  |   Il s'agit d'un nouveau test 
action_result.data.\*.word_count | numeric |  |   5 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 