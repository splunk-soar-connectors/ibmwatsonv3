[comment]: # "Auto-generated SOAR connector documentation"
# Watson \- Language Translator V3

Publisher: Splunk  
Connector Version: 1\.0\.1  
Product Vendor: IBM  
Product Name: Watson Language Translator V3  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

Leverage IBM Watson for language translation using API version V3

[comment]: # " File: readme.md"
[comment]: # "  Copyright (c) 2021 Splunk Inc."
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
**base\_url** |  required  | string | Watson URL
**verify\_server\_cert** |  optional  | boolean | Verify server certificate
**api\_key** |  required  | password | Watson API key
**version** |  optional  | string | Watson current API version \(YYYY\-MM\-DD\)

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
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.text | string | 
action\_result\.data\.\*\.confidence | numeric | 
action\_result\.data\.\*\.language | string |  `language` 
action\_result\.data\.\*\.languages\.\*\.confidence | numeric | 
action\_result\.data\.\*\.languages\.\*\.language | string | 
action\_result\.summary\.high\_confidence\_match | string |  `language` 
action\_result\.summary\.total\_languages | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list languages'
List languages that can be used for translation

Type: **generic**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.data\.\*\.language | string |  `language` 
action\_result\.data\.\*\.name | string | 
action\_result\.summary\.total\_languages | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list translations'
List languages translation models

Type: **generic**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.data\.\*\.base\_model\_id | string | 
action\_result\.data\.\*\.customizable | boolean | 
action\_result\.data\.\*\.default\_model | boolean | 
action\_result\.data\.\*\.domain | string |  `domain` 
action\_result\.data\.\*\.model\_id | string |  `watson translation model` 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.owner | string | 
action\_result\.data\.\*\.source | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.target | string | 
action\_result\.data\.\*\.training\_log | string | 
action\_result\.summary\.total\_models | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'translate text'
Translate text from one language to another

Type: **generic**  
Read only: **True**

If model\_id is specified the source and target parameters are ignored\.<br>If the action fails with the error <i>Model not found</i>, it means the service cannot translate the text as is and a customized model needs to be created\. Please see the Watson Language Translator documentation for instructions on creating a customized model\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**text** |  required  | Text to translate | string | 
**source** |  optional  | Source language | string |  `language` 
**target** |  optional  | Target language | string |  `language` 
**model\_id** |  optional  | Translation Model | string |  `watson translation model` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.model\_id | string |  `watson translation model` 
action\_result\.parameter\.source | string |  `language` 
action\_result\.parameter\.target | string |  `language` 
action\_result\.parameter\.text | string | 
action\_result\.data\.\*\.character\_count | numeric | 
action\_result\.data\.\*\.translations\.\*\.translation | string | 
action\_result\.data\.\*\.word\_count | numeric | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 