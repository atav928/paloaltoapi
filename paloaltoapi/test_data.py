# pylint: disable=too-many-lines
"""Test Data"""

PANORAMA_DAG_XML = b'''<response status="success">
    <result>
        <device-groups>
            <entry name="shared">
                <address-group name="dag-dev-adplat-app">
                    <filter>\'_nsx_app-adplat-app-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-adplat-pre">
                    <filter>\'app-adplat-pre-sg-41\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-devops-all">
                    <filter>\'env-development-sg-11\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-devops-app">
                    <filter>\'svc-1-role-app-sg-20\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-devops-pres">
                    <filter>\'svc-1-role-pres-sg-22\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-devops-database">
                    <filter>\'svc-1-role-database-sg-21\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-devops-all">
                    <filter>\'svc-1-ALL_PROD_NETWORK-sg-10\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-BAD-BAD-Tag-Members">
                    <filter>\'BAD-BAD-TAG-sg-38\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-devops-app">
                    <filter>\'role-app-sg-15\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-devops-database">
                    <filter>\'role-database-sg-17\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-devops-pres">
                    <filter>\'role-pres-sg-16\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-devops-all">
                    <filter>\'svc-1-env-pd-sg-15\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-devops-app">
                    <filter>\'svc-1-env-pd-sg-15\' and \'svc-1-role-app-sg-25\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-devops-database">
                    <filter>\'svc-1-env-pd-sg-15\' and \'svc-1-role-database-sg-26\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-devops-pres">
                    <filter>\'svc-1-env-pd-sg-15\' and \'svc-1-role-pres-sg-27\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-net-devops-sandbox-all">
                    <filter>\'ALL-SANDBOX-NETWORKS-sg-20\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-devops-all">
                    <filter>\'svc-2-env-qa-sg-16\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-devops-app">
                    <filter>\'svc-2-env-qa-sg-16\' and \'svc-2-role-app-sg-25\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-devops-database">
                    <filter>\'svc-2-env-qa-sg-16\' and \'svc-2-role-database-sg-26\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-devops-pres">
                    <filter>\'svc-2-env-qa-sg-16\' and \'svc-2-role-pres-sg-27\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-adplat-app">
                    <filter>\'svc-1-app-adplat-app-sg-30\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-adplat-pre">
                    <filter>\'svc-1-app-adplat-pre-sg-32\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-releaseautoman-app">
                    <filter>\'svc-1-app-releaseautoman-app-sg-36\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-releaseautoman-pres">
                    <filter>\'svc-1-app-releaseautoman-pre-sg-37\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-releaseautoman-app">
                    <filter>\'svc-2-app-releaseautoman-app-sg-37\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-releaseautoman-pres">
                    <filter>\'svc-2-app-releaseautoman-pre-sg-38\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-productcatalog">
                    <filter>\'svc-1-app-productcatalog-sg-38\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-adplat">
                    <filter>\'svc-1-app-adplat-sg-40\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-adplat">
                    <filter>\'app-adplat-app-sg-30\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-adplat">
                    <filter>\'app-adplat-app-sg-30\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-adplat">
                    <filter>\'app-adplat-sg-40\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-productcatalog">
                    <filter>\'app-productcatalog-sg-38\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-productcatalog">
                    <filter>\'app-productcatalog-sg-50\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-qa-productcatalog">
                    <filter>\'app-productcatalog-sg-38\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-ext-access-docker">
                    <filter>\'ext-access-docker-sg-45\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-releaseautoman">
                    <filter>\'svc-1-app-releaseautoman-sg-41\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-acats">
                    <filter>\'svc-1-app-ACATS-sg-46\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chef">
                    <filter>\'svc-1-app-chef-sg-47\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-model">
                    <filter>\'svc-1-app-model-app-sg-49\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-apacheSOLR-pres">
                    <filter>\'svc-1-app-apache-solr-pre-sg-50\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-lucidworksfusion-app">
                    <filter>\'svc-1-app-lucidworksfusion-app-sg-51\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-apache-solr-app">
                    <filter>\'svc-1-app-apache-solr-app-sg-52\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chef-app">
                    <filter>\'svc-1-app-chef-sg-47\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-esflows-app">
                    <filter>\'svc-1-app-esflows-sg-54\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-transitionmgmt">
                    <filter>\'svc-1-app-transitionmgmt-sg-55\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-clientonboarding">
                    <filter>\'svc-1-app-clientonboarding-sg-56\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-trustmfrecon">
                    <filter>\'svc-1-app-trustmfrecon-sg-59\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-trustcashsweep">
                    <filter>\'svc-1-app-trustcashsweep-sg-58\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-advancedsearch">
                    <filter>svc-1-app-advancedsearch-sg-57</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-marketingcontentproxy">
                    <filter>svc-1-app-marketingcontentproxy-sg-60</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-apache-solr">
                    <filter>\'svc-1-app-apache-solr-sg-61\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-zookeeper">
                    <filter>\'svc-1-app-zookeeper-sg-62\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-kafka-pres">
                    <filter>\'svc-1-app-kafka-pres-sg-63\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-kafka-app">
                    <filter>\'svc-1-app-kafka-app-sg-64\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-kafka-mgmt">
                    <filter>\'svc-1-app-kafka-mgmt-sg-65\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-RancherK8sDevOps-mgmt">
                    <filter>\'svc-1-app-RancherK8sDevOps-mgmt-sg-66\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-hw-mgmt">
                    <filter>\'svc-1-app-hw-mgmt-sg-67\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-crm-app">
                    <filter>\'svc-1-app-crm-app-sg-68\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-crm-pres">
                    <filter>\'svc-1-app-crm-pres-sg-69\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefaai-app">
                    <filter>\'svc-1-app-chefaai-app-sg-77\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefdpe-app">
                    <filter>\'svc-1-app-chefdpe-app-sg-75\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefaai-mgmt">
                    <filter>\'svc-1-app-chefaai-mgmt-sg-78\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefdcl-app">
                    <filter>\'svc-1-app-chefdcl-app-sg-73\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chef-mgmt">
                    <filter>\'svc-1-app-chef-mgmt-sg-70\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefas-mgmt">
                    <filter>\'svc-1-app-chefas-mgmt-sg-72\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefdpe-mgmt">
                    <filter>\'svc-1-app-chefdpe-mgmt-sg-76\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefdcl-mgmt">
                    <filter>\'svc-1-app-chefdcl-mgmt-sg-74\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-chefas-app">
                    <filter>\'svc-1-app-chefas-app-sg-71\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-essearchcrm">
                    <filter>\'svc-1-app-essearchcrm-sg-79\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-foresct_shared">
                    <filter>\'ForeScout-blockPing\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dev-foresct_test">
                    <filter>ForeScout-blockPing\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-s3ecs-app">
                    <filter>\'svc-1-app-s3ecs-app-sg-80\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-s3ecs-mgmt">
                    <filter>\'svc-1-app-s3ecs-mgmt-sg-81\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-fiimpact">
                    <filter>\'svc-1-app-fiimpact-sg-83\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-essearch">
                    <filter>\'svc-1-app-essearch-sg-84\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-securityutilityplatform">
                    <filter>\'svc-1-app-securityutilityplatform-sg-85\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-sitecore">
                    <filter>\'svc-1-app-sitecore-sg-82\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-BlueMatrixResearchIntegr">
                    <filter>\'svc-1-app-BlueMatrixResearchIntegr-sg-86\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-devops-management">
                    <filter>svc-1-role-management-sg-89</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-fullypaidlending">
                    <filter>svc-1-app-fullypaidlending-sg-90</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-PCGFileTransmissions">
                    <filter>\'svc-1-app-PCGFileTransmissions-sg-92\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ProducersChoiceNetwork">
                    <filter>\'svc-1-app-ProducersChoiceNetwork-sg-91\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-rto">
                    <filter>\'svc-1-app-rto-sg-93\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-simonplus">
                    <filter>\'svc-1-app-simonplus-sg-95\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-pd-VulnerabilityRptgSvc">
                    <filter>\'svc-1-app-VulnerabilityRptgSvc-sg-97\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-pd-advisor-texting">
                    <filter>\'svc-1-app-AdvisorTexting-sg-96\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ESAddressValidation">
                    <filter>\'svc-1-app-ESAddressValidation-sg-98\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-StructuredInvestments">
                    <filter>\'svc-1-app-StructuredInvestments-sg-99\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-role-app">
                    <filter>\'role-app\' and \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-role-web">
                    <filter>\'role-web\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-basetech-jboss">
                    <filter>\'basetech-jboss\' AND \'env-dev\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-basetech-apache">
                    <filter>\'basetech-apache\' AND \'env-dev\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-releaseautoman">
                    <filter>\'altci-releaseautoman\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="g-sample-DAG">
                    <filter>\'sample-TAG\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-TrustDataMart">
                    <filter>svc-1-app-TrustDataMart-sg-100</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-MIDAS">
                    <filter>\'svc-1-app-MIDAS-sg-101\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-TradingSys">
                    <filter>\'svc-1-app-TradingSys-app-sg-102\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-secb">
                    <filter>\'svc-1-app-secb-sg-104\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-secbOrig">
                    <filter>\'svc-1-app-secbOrig-sg-103\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-FixedIncomeMsgInterface">
                    <filter>\'svc-1-app-FixedIncomeMsgInterface-sg-105\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-role-app">
                    <filter>\'role-app\' and \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-role-web">
                    <filter>\'role-web\' and \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-basetech-jboss">
                    <filter>\'basetech-jboss\' and \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-TaxWithholding">
                    <filter>\'svc-1-app-TaxWithholding-sg-106\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-hwsolr">
                    <filter>svc-1-app-hwsolr-sg-108</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-CDSAnalysis">
                    <filter>\'svc-1-app-CDSAnalysis-sg-109\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ProofpointSupervision">
                    <filter>svc-1-app-ProofpointSupervision-sg-110</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-basetech-apache">
                    <filter>\'basetech-apache\' AND \'env-qa\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-releaseautoman">
                    <filter>\'altci-releaseautoman\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-basetech-jboss">
                    <filter>\'basetech-jboss\' and \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-role-web">
                    <filter>\'role-web\' and \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-role-app">
                    <filter>\'role-app\' and \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-pbrtool">
                    <filter>svc-1-app-pbrtool-mgmt-sg-113\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-elasticsearch">
                    <filter>\'altci-elasticsearch\' AND \'env-prod\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esaddressvalidation">
                    <filter>\'altci-esaddressvalidation\' AND \'env-prod\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-esaddressvalidation">
                    <filter>\'altci-esaddressvalidation\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-esaddressvalidation">
                    <filter>\'altci-esaddressvalidation\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-elasticsearch">
                    <filter>\'altci-elasticsearch\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-elasticsearch">
                    <filter> \'altci-elasticsearch\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-picdeskapisvc">
                    <filter>\'svc-1-app-PICDesk-sg-114\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-PartnerMgmtPlatform">
                    <filter>\'svc-1-app-PartnerMgmtPlatform-sg-115\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ESRestriction">
                    <filter>svc-1-app-ESRestriction-sg-116</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-MarginAnalysis">
                    <filter>svc-1-app-MarginAnalysis-sg-94</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="svc-4-app-ProofpointSupervision-sg-104">
                    <filter>svc-4-app-TrustDataMart-sg-87</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-MIDAS">
                    <filter>\'svc-4-app-MIDAS-sg-99\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-PCGFileTransmissions">
                    <filter>\'svc-4-app-PCGFileTransmissions-sg-101\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-TrustDataMart">
                    <filter>\'svc-4-app-TrustDataMart-sg-87\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-PartnerMgmtPlatform">
                    <filter>\'svc-4-app-PartnerMgmtPlatform-sg-102\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-ProducersChoiceNetwork">
                    <filter>\'svc-4-app-ProducersChoiceNetwork-sg-103\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-hw-mgmt">
                    <filter>\'svc-4-app-hw-mgmt-sg-98\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-ProofpointSupervision">
                    <filter>\'svc-4-app-ProofpointSupervision-sg-104\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-rto">
                    <filter>\'svc-4-app-rto-sg-83\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-MarginAnalysis">
                    <filter>\'svc-4-app-MarginAnalysis-sg-100\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradecorrections">
                    <filter>\'svc-1-app-TradeCorrections-sg-117\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-weeklydigestcms">
                    <filter>\'svc-1-app-WeeklyDigestCMS-sg-118\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-wealthmgmt">
                    <filter>\'svc-1-app-WealthMgmt-sg-119\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-TradingSysCache">
                    <filter>\'svc-1-app-TradingSysCache-sg-121\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradingbusinessengine">
                    <filter>\'svc-1-app-tradingbusinessengine-sg-122\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradingcollabengine">
                    <filter>\'svc-1-app-tradingcollabengine-sg-123\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradingsyscssint">
                    <filter>\'svc-1-app-tradingsyscssint-sg-124\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradingsyscssintconsumer">
                    <filter>\'svc-1-app-tradingsyscssintconsumer-sg-125\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradingsysomdint">
                    <filter>\'svc-1-app-tradingsysomdint-sg-126\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradingsysrpts">
                    <filter>\'svc-1-app-tradingsysrpts-sg-127\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ESHierarchySearch">
                    <filter>\'svc-1-app-ESHierarchySearch-sg-128\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-AMSPPMx">
                    <filter>\'svc-1-app-AMSPPMx-sg-130\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-eFolioPlus">
                    <filter>\'svc-1-app-eFolioPlus-sg-129\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-elm">
                    <filter>svc-1-app-elm-sg-131</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-esnotifications">
                    <filter>\'svc-1-app-esnotifications-sg-132\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-tradeconfirmations">
                    <filter>\'svc-1-app-TradeConfirmations-sg-133\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-BankResMortgage">
                    <filter>\'svc-1-app-BankResMortgage-sg-134\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-FISharedServices">
                    <filter>\'svc-1-app-FISharedServices-sg-136\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-svccenterscratchpad">
                    <filter>\'altci-svccenterscratchpad\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-releaseautoman">
                    <filter>\'altci-releaseautoman\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-svccenterscratchpad">
                    <filter>\'altci-svccenterscratchpad\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-svccenterscratchpad">
                    <filter>\'altci-svccenterscratchpad\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-IntelledoxInfiniti">
                    <filter>\'svc-1-app-IntelledoxInfiniti-sg-137\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-trustmfrecon">
                    <filter>\'altci-trustmfrecon\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-trustmfrecon">
                    <filter>\'altci-trustmfrecon\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-trustmfrecon">
                    <filter>\'altci-trustmfrecon\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-classactionlawsuitsys">
                    <filter>\'altci-classactionlawsuitsys\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-classactionlawsuitsys">
                    <filter>\'altci-classactionlawsuitsys\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-classactionlawsuitsys">
                    <filter>\'altci-classactionlawsuitsys\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-consolidatedstockrecord">
                    <filter>\'altci-consolidatedstockrecord\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-consolidatedstockrecord">
                    <filter>\'altci-consolidatedstockrecord\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-consolidatedstockrecord">
                    <filter>\'altci-consolidatedstockrecord\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-FormRepository">
                    <filter>\'svc-1-app-FormRepository-sg-138\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-eseligibility">
                    <filter>\'svc-1-app-ESEligibility-sg-139\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-environment-dev">
                    <filter>\'env-dev\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-environment-qa">
                    <filter>\'env-qa\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-environment-prod">
                    <filter>\'env-prod\'\n</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-transitionmgmt">
                    <filter>\'altci-transitionmgmt\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-transitionmgmt">
                    <filter>\'altci-transitionmgmtcob\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-transitionmgmt">
                    <filter>\'altci-transitionmgmt\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-trustcashsweep">
                    <filter>\'altci-trustcashsweep\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-trustcashsweep">
                    <filter>\'altci-trustcashsweep\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-trustcashsweep">
                    <filter>\'altci-trustcashsweep\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-massaccttransconv">
                    <filter>\'svc-1-app-MassAcctTransConversion-sg-141\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-reportexecenterprise">
                    <filter>\'altci-reportexecenterprise\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-forwardmarginsystem">
                    <filter>\'altci-forwardmarginsystem\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-forwardmarginsystem">
                    <filter>\'altci-forwardmarginsystem\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-forwardmarginsystem">
                    <filter>\'altci-forwardmarginsystem\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-1099process">
                    <filter>\'altci-1099process\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-1099process">
                    <filter>\'altci-1099process\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-1099process">
                    <filter>\'altci-1099process\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-PCGPortal">
                    <filter>\'svc-1-app-PCGPortal-sg-142\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-FiMATS">
                    <filter>\'svc-1-app-FiMATS-sg-143\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ITCFAdoptions">
                    <filter>\'svc-1-app-ITCFAdoptions-sg-145\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ConflictsOfInterest">
                    <filter>\'svc-1-app-ConflictsOfInterest-sg-144\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ECMAdministration">
                    <filter>\'svc-1-app-ECMAdministration-sg-146\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-CustomerIdentificationPgrm">
                    <filter>\'svc-1-app-CustomerIdentificationPgrm-sg-148\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-PracticeCenter">
                    <filter>\'svc-1-app-PracticeCenter-sg-147\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-AlternativeInvestments">
                    <filter>\'svc-1-app-AlternativeInvestments-sg-149\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ProposalGeneration">
                    <filter>\'svc-1-app-ProposalGeneration-sg-152\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-GoalPlanningandMonitoring">
                    <filter>\'svc-1-App-GoalPlanningandMonitoring-sg-153\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-TradeClearance">
                    <filter>\'svc-1-app-TradeClearance-sg-155\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-PCGBusinessDevelopment">
                    <filter>\'svc-1-app-PCGBusinessDevelopment-sg-156\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-dr-ExternalAcctsAgg">
                    <filter>\'svc-1-app-ExternalAcctsAgg-sg-157\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-CTAPortal">
                    <filter>\'svc-1-app-CTAPortal-sg-158\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-TaxCreditFundsSys">
                    <filter>\'svc-1-app-TaxCreditFundsSys-sg-159\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ClientReporting">
                    <filter>\'svc-1-app-ClientReporting-sg-135\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-crimson">
                    <filter>\'svc-1-app-crimson-sg-160\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-BrokerageStatementDV">
                    <filter>\'svc-1-app-BrokerageStatementDV-sg-161\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prd-ProductRiskRating">
                    <filter>\'svc-1-App-ProductRiskRating-sg-162\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ClientServiceMgmt">
                    <filter>\'svc-1-app-ClientServiceMgmt-sg-163\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-IGSys">
                    <filter>\'svc-1-App-IGSys-sg-164\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-AMSBilling">
                    <filter>\'svc-1-app-AMSBilling-sg-165\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-RancherK8sDevOps">
                    <filter>\'altci-RancherK8sDevOps\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-clientcentercacheredis">
                    <filter>\'svc-1-app-clientcentercacheredis-sg-166\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-clientaccesscacheredis">
                    <filter>\'svc-1-app-clientaccesscacheredis-sg-167\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-clientsharedcacheredis">
                    <filter>\'svc-1-app-clientsharedcacheredis-sg-168\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-icom">
                    <filter>\'svc-1-app-icom-sg-169\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prd-ESPrql">
                    <filter>\'svc-1-App-ESPrql-sg-170\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-markitctitaxsolut">
                    <filter>\'altci-markitctitaxsolut\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-markitctitaxsolut">
                    <filter>\'altci-markitctitaxsolut\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-markitctitaxsolut">
                    <filter>\'altci-markitctitaxsolut\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prd-pcgdeals">
                    <filter>\'svc-1-App-pcgdeals-sg-171\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ESPersonSvc">
                    <filter>\'svc-1-App-ESPersonSvc-sg-172\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-esasset">
                    <filter>\'svc-1-app-esasset-sg-173\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-MutualFundDashboard">
                    <filter>\'svc-1-App-MutualFundDashboard-sg-176\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-MisysLoanIQ">
                    <filter>\'svc-1-app-MisysLoanIQ-sg-177\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ClientOnboardingInst">
                    <filter>\'svc-1-App-ClientOnboardingInst-sg-179\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ADAMgmt">
                    <filter>\'svc-1-App-ADAMgmt-sg-182\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-hwre">
                    <filter>\'svc-1-app-hwre-sg-150\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-redis">
                    <filter>\'svc-1-app-redis-sg-183\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-EcommMachineLearning">
                    <filter>\'svc-1-app-EcommMachineLearning-sg-184\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-RancherK8sDevOps">
                    <filter>\'altci-RancherK8sDevOps\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-RancherK8sDevOps">
                    <filter>\'altci-RancherK8sDevOps\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-InterestMgmtSys">
                    <filter>\'svc-1-app-InterestMgmtSys-sg-185\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-jolt">
                    <filter>\'svc-1-app-jolt-sg-186\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-nac-isolate">
                    <filter>\'isolate\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-nac-isolate-int">
                    <filter>\'isolate-int\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-risk">
                    <filter>\'svc-1-app-risk-sg-188\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-IRMDataLibrary">
                    <filter>\'svc-1-app-IRMDataLibrary-sg-190\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-rmb">
                    <filter>\'svc-1-app-rmb-sg-189\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ESignature">
                    <filter>\'svc-1-app-ESignature-sg-192\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-GoalPlanningandMonitoring">
                    <filter>\'svc-1-App-GoalPlanningandMonitoring-sg-153\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-OMSToolKit">
                    <filter>\'svc-1-app-OMSToolkit-sg-194\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-tradingsys">
                    <filter>\'altci-tradingsys\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-eseligibility">
                    <filter>\'altci-eseligibility\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-esnotifications">
                    <filter>\'altci-esnotifications\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-essearch">
                    <filter>\'altci-essearch\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-tradingsys">
                    <filter>\'altci-tradingsys\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-tradingsys">
                    <filter>\'altci-tradingsys\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-eseligibility">
                    <filter>\'altci-eseligibility\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-eseligibility">
                    <filter>\'altci-eseligibility\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-esnotifications">
                    <filter>\'altci-esnotifications\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esnotifications">
                    <filter>\'altci-esnotifications\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-essearch">
                    <filter>\'altci-essearch\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-essearch">
                    <filter>\'altci-essearch\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-AMLRes">
                    <filter>\'svc-1-app-AMLRe-sg-195\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-trustdatamart">
                    <filter>\'altci-trustdatamart\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-rto">
                    <filter>\'altci-rto\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-secb">
                    <filter>\'altci-secb\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-cts">
                    <filter>\'svc-1-app-cts-sg-196\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-qn">
                    <filter>\'svc-1-app-qn-sg-197\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-rcld">
                    <filter>\'svc-1-app-rcld-sg-198\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-StandardTrades">
                    <filter>\'svc-1-app-StandardTrades-sg-199\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-trustdatamart">
                    <filter>\'altci-trustdatamart\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-trustdatamart">
                    <filter>\'altci-trustdatamart\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-rto">
                    <filter>\'altci-rto\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-rto">
                    <filter>\'altci-rto\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-elm">
                    <filter>\'altci-elm\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-elm">
                    <filter>\'altci-elm\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-elm">
                    <filter>\'altci-elm\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-sitecorenet">
                    <filter>\'altci-sitecorenet\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-sitecorenet">
                    <filter>\'altci-sitecorenet\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-producerschoicenetwork">
                    <filter>\'altci-producerschoicenetwork\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-sitereliabilityeng">
                    <filter>\'altci-sitereliabilityeng\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-tradeclearance">
                    <filter>\'altci-tradeclearance\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-ecommmachinelearning">
                    <filter>\'altci-ecommmachinelearning\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-ecommmachinelearning">
                    <filter>\'altci-ecommmachinelearning\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-ecommmachinelearning">
                    <filter>\'altci-ecommmachinelearning\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-hw">
                    <filter>\'altci-hw\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-hw">
                    <filter>\'altci-hw\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-hw">
                    <filter>\'altci-hw\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-simonplus">
                    <filter>\'altci-simonplus\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-simonplus">
                    <filter>\'altci-simonplus\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-simonplus">
                    <filter>\'altci-simonplus\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-ESUserMetrics">
                    <filter>\'altci-esusermetrics\' and \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-ESUserMetrics">
                    <filter>\'altci-esusermetrics\' and \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-espartyproxy">
                    <filter>\'altci-ESPartyProxy\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-icom">
                    <filter>\'altci-icom\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-devopsjupyterhub">
                    <filter>\'altci-devopsjupyterhub\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-practicecenter">
                    <filter>\'altci-practicecenter\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-ctaportal">
                    <filter>\'altci-ctaportal\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-ctaportal">
                    <filter>\'altci-ctaportal\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-ctaportal">
                    <filter>\'altci-ctaportal\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-fisharedservices">
                    <filter>\'altci-fisharedservices\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-ServiceCenterApprovals">
                    <filter>\'svc-1-app-ServiceCenterApprovals-sg-202\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-legacyjournals">
                    <filter>\'altci-legacyjournals\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-legacyjournals">
                    <filter>\'altci-legacyjournals\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-tradeclearance">
                    <filter>\'altci-tradeclearance\' AND \'env-dev\' </filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-secbOrig">
                    <filter>\'altci-secborig\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-tradeconfirmations">
                    <filter>\'altci-tradeconfirmations\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-tradeconfirmations">
                    <filter>\'altci-tradeconfirmations\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-tradeconfirmations">
                    <filter>\'altci-tradeconfirmations\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-esapimanagementpoc">
                    <filter>\'altci-esapimanagementpoc\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esapimanagementpoc">
                    <filter>\'altci-esapimanagementpoc\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-esapimanagementpoc">
                    <filter>\'altci-esapimanagementpoc\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-proofpointsupervision">
                    <filter>\'altci-proofpointsupervision\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-proofpointsupervision">
                    <filter>\'altci-proofpointsupervision\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-proofpointsupervision">
                    <filter>\'altci-proofpointsupervision\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-advisortexting">
                    <filter>\'altci-advisortexting\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-advisortexting">
                    <filter>\'altci-advisortexting\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-advisortexting">
                    <filter>\'altci-advisortexting\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-elmpassport">
                    <filter>\'altci-elmpassport\' and \'anv-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-adplat">
                    <filter>\'altci-adplat\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-massaccttransconversion">
                    <filter>\'altci-massaccttransconversion\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-efolioplus">
                    <filter>\'altci-efolioplus\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esmarketdatafeed">
                    <filter>\'altci-esmarketdatafeed\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-productdetail">
                    <filter>\'altci-productdetail\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esccsibusiness">
                    <filter>\'altci-esccsibusiness\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-massaccttransconversion">
                    <filter>\'altci-massaccttransconversion\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-massaccttransconversion">
                    <filter>\'altci-massaccttransconversion\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esarrangement">
                    <filter>\'altci-esarrangement\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esparty">
                    <filter>\'altci-esparty\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-adamgmt">
                    <filter>\'altci-adamgmt\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-wealthmgmt">
                    <filter>\'altci-wealthmgmt\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-esasset">
                    <filter>\'altci-esasset\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-qa-personaltradepreclearance">
                    <filter>\'altci-personaltradepreclearance\' AND \'env-qa\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-personaltradepreclearance">
                    <filter>\'altci-personaltradepreclearance\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-dev-personaltradepreclearance">
                    <filter>\'altci-personaltradepreclearance\' AND \'env-dev\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-productcatalog">
                    <filter>\'altci-productcatalog\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-model">
                    <filter>\'altci-model\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="grp-auto-prod-taxcreditfundssys">
                    <filter>\'altci-taxcreditfundssys\' AND \'env-prod\'</filter>
                    <member-list></member-list>
                </address-group>
            </entry>
            <entry name="Datacenter"></entry>
            <entry name="Vendor"></entry>
            <entry name="Remote"></entry>
            <entry name="Untrest_DMZ"></entry>
            <entry name="GlobalProtect">
                <address-group name="dag-test-isolate">
                    <filter>\'isolate\'</filter>
                    <member-list></member-list>
                </address-group>
            </entry>
            <entry name="ESX">
                <address-group name="dag-prod-opps">
                    <filter>\'svc-1-app-opps-sg-201\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="NSX_PG_pres">
                    <filter>\'Port Group pres-sg-27\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="dag-prod-blpXVAIntegration">
                    <filter>\'svc-1-app-blpXVAIntegration-sg-200\'</filter>
                    <member-list></member-list>
                </address-group>
                <address-group name="BAD-BAD-TAG">
                    <filter>\'BAD-BAD-TAG-sg-26\'</filter>
                    <member-list></member-list>
                </address-group>
            </entry>
            <entry name="Development">
                <address-group name="dag-dev-foresct_test">
                    <filter>\'ForeScout-blockPing\'</filter>
                    <member-list></member-list>
                </address-group>
            </entry>
        </device-groups>
    </result>
</response>'''
