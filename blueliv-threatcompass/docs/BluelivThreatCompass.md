## About the connector
Blueliv ThreatCompass systematically looks for information about companies,products, people, brands, logos, assets, technology and other information, depending on your needs. Blueliv ThreatCompass allows you to monitor and track all this information to keep your data, your organization and its employees safe
<p>This document provides information about the Blueliv ThreatCompass Connector, which facilitates automated interactions, with a Blueliv ThreatCompass server using FortiSOAR&trade; playbooks. Add the Blueliv ThreatCompass Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Blueliv ThreatCompass.</p>
### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-blueliv-threatcompass</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Blueliv ThreatCompass server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Blueliv ThreatCompass server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Blueliv ThreatCompass</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the IP address or hostname of the ThreatCompass server to which you will connect and perform automated operations.
</td>
</tr><tr><td>API Token</td><td>Specify the API Key which is associated to your account that you will use to access the ThreatCompass REST API.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Resource List</td><td>Retrieves the list of Resources for the specified Organization and Module</td><td>get_resource_list <br/>Investigation</td></tr>
<tr><td>Get Resource by ID</td><td>Retrieves the Resource for the specified Organization and Module based on Resource ID</td><td>get_resource <br/>Investigation</td></tr>
<tr><td>Update Resource Status</td><td>Modifies the Resource status for the specified Organization and Module based on Resource ID and status</td><td>update_resource_status <br/>Investigation</td></tr>
<tr><td>Update Resource Label</td><td>Modifies the Resource Label for the specified Organization and Module based on Resource ID and Label</td><td>update_resource_label <br/>Investigation</td></tr>
<tr><td>Update Resource Read Status</td><td>Modifies the Read Status of Resource for the specified Organization and Module based on Resource ID</td><td>update_resource_read_status <br/>Investigation</td></tr>
<tr><td>Update Resource Rating</td><td>Modifies the Rating of Resource for the specified Organization and Module based on Resource ID</td><td>update_resource_rating <br/>Investigation</td></tr>
<tr><td>Update Resource FAV</td><td>Modifies the Favourite Status of Resource for the specified Organization and Module based on Resource ID</td><td>update_resource_fav <br/>Investigation</td></tr>
<tr><td>Update Resource TLP</td><td>Modifies the TLP Status of Resource for the specified Organization and Module based on Resource ID</td><td>update_resource_tlp <br/>Investigation</td></tr>
<tr><td>Get Module Labels</td><td>Retrieves the label list of the module for the specified Organization and Module ID</td><td>get_module_labels <br/>Investigation</td></tr>
</tbody></table>
### operation: Get Resource List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>To</td><td>Specify the exclusive Upper limit Date(in milliseconds) with which results before this date will be fetched.'Since' param will be calculated to a maximum of one-year limit from this date.
</td></tr><tr><td>Since</td><td>Specify the exclusive Lower limit Date(in milliseconds) to which results after this date will be fetched. Limited to a maximum of one year If no date is given or it's more than a year from the current date or 'To' parameter.
</td></tr><tr><td>Page</td><td>Specify the Page number whose result you want to fetch. Default value is 1
</td></tr><tr><td>Limit</td><td>Specify the maximum amount of results to retrieve. Default value is 10
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Get Resource by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Resource ID</td><td>Specify the ID of the Resource which you want to fetch
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Update Resource Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Module Type</td><td>Specify the Module Type to which you want to filter the results
</td></tr><tr><td>Resource ID</td><td>Specify the ID of the resource which you want to fetch
</td></tr><tr><td>Status</td><td>Specify the new Status to be assigned to the Resource
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Update Resource Label
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Module Type</td><td>Specify the Module Type to which you want to filter the results
</td></tr><tr><td>Resource ID</td><td>Specify the ID (Comma Separated Values) of the Resource which you want to update
</td></tr><tr><td>Label ID</td><td>Specify the Label ID to be assigned to the Resource
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Update Resource Read Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Module Type</td><td>Specify the Module Type to which you want to filter the results
</td></tr><tr><td>Resource ID</td><td>Specify the ID (Comma Separated Values) of the Resource which you want to update
</td></tr><tr><td>Read Status</td><td>Check if you want to mark this resource as read
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Update Resource Rating
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Module Type</td><td>Specify the Module Type to which you want to filter the results
</td></tr><tr><td>Resource ID</td><td>Specify the ID (Comma Separated Values) of the Resource which you want to update
</td></tr><tr><td>Rating</td><td>Specify the Rating that you want to assign the specified resource
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Update Resource FAV
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Module Type</td><td>Specify the Module Type to which you want to filter the results
</td></tr><tr><td>Resource ID</td><td>Specify the ID (Comma Separated Values) of the Resource which you want to update
</td></tr><tr><td>FAV Status</td><td>Specify the FAV Status which you want to assign the specified resource
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Update Resource TLP
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Module Type</td><td>Specify the Module Type to which you want to filter the results
</td></tr><tr><td>Resource ID</td><td>Specify the ID of the Resource which you want to update
</td></tr><tr><td>TLP Status</td><td>Specify the TLP Status which you want to assign the specified resource
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Get Module Labels
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the Organization ID with which you want to filter the results. Specify the value 0 to Get Results from all organizations.
</td></tr><tr><td>Module ID</td><td>Specify the Module ID with which you want to filter the results. Specify the value 0 to Get Results from all Modules
</td></tr><tr><td>Module Type</td><td>Specify the Module Type to which you want to filter the results
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to ThreatCompass REST API Documentation
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - blueliv-threatcompass - 1.0.0` playbook collection comes bundled with the Blueliv ThreatCompass connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Blueliv ThreatCompass connector.

- Get Module Labels
- Get Resource
- Get Resource List
- Set Resource FAV
- Set Resource Label
- Set Resource Rating
- Set Resource Read Status
- Set Resource Status
- Set Resource TLP

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
