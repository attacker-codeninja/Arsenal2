#!/bin/bash

if [ -t 0 ]; then
  echo "Usage: cat input | $0"
  exit 1
fi

input=$(cat)

declare -A cms_patterns=(
  ["wordpress"]="wordpress|wp|wp engine|powered by wordpress"
  ["jira"]="jira|confluence|atlassian|bitbucket|bamboo"
  ["drupal"]="drupal|drupal cms"
  ["joomla"]="joomla|joomla cms|joomla version"
  ["ecommerce"]="magento|shopify|prestashop|opencart|bigcommerce|woocommerce|nopcommerce|saleor|sylius|miva|vtiger"
  ["general"]="typo3|umbraco|dotnetnuke|plone|ghost|strapi|orchard|silverstripe|textpattern|weebly|squarespace|duda|sitefinity|cmsmadesimple|serendipity|aem|kentico|openpublic|civicspace"
  ["forums"]="xenforo|vbulletin|phpbb|discourse|vanilla forums|mybb|fudforum|simple machines forum|fluxbb"
  ["education"]="moodle|blackboard|sakai|canvas lms|dokeos|claroline"
  ["portal"]="liferay|wix|jimdo|zoho sites|webflow|webnode|djangocms|mezzanine|pyrocms|bolt cms|statamic|bludit|episerver"
  ["php"]="phpmyadmin|cakephp|codeigniter|fuelphp|zend framework|laravel|yii framework|symfony"
  ["wiki"]="mediawiki|tiki wiki|twiki|xwiki|dokuwiki"
  ["static"]="jekyll|hugo|gatsby|netlify cms|pelican"
  ["government"]="govcms|openpublic|civicspace"
  ["enterprise"]="sitecore|kentico|episerver|dotcms|opentext|adobe experience manager|aem"
  ["servers"]="iis|apache|nginx|tomcat|gunicorn|uwsgi|express|lighttpd|jetty|centos"
  ["admin_panels"]="admin|administrator|controlpanel|cpanel|backend|login|auth|secure|support|helpdesk|manage|dashboard|signin|admin dashboard|user/login|admin/login"
  ["sensitive_subdomains"]="staging|test|dev|qa|beta|uat|internal|secure|private|backup|old|demo|sandbox|preprod|mail|email|smtp|imap|pop3|static|debug|logs"
  ["open_directories"]="index of|directory listing|file listing|parent directory|dir browse|directory contents|open directory|file explorer|browsable directory"
  ["api_endpoints"]="api|rest api|graphql|swagger|openapi|postman|http api|json|xml|soap|api docs"
  ["clouds"]="aws|amazon s3|google cloud|gcp|heroku|digitalocean|linode|vultr|rackspace|bucket"
  ["dashboard_setup"]="setup|wizard|install|installation|onboarding|config|configuration|setup wizard|first time setup|setup dashboard|init|initialization|setup/login"
  ["titles"]="powered by|index of|welcome to|hosted by|proudly served by|dashboard|login page|home page|sign in|error page|403 forbidden|404 not found|500 internal server error|access denied|service unavailable"
  ["frameworks"]="django|flask|spring boot|rails|asp.net|laravel|codeigniter|express|fastapi|symfony|nestjs|react|angular|vue|svelte"
  ["databases"]="mysql|mariadb|postgresql|mongo|redis|sqlite|oracle|mssql|couchdb|dynamodb"
  ["technologies"]="nginx|apache|iis|tomcat|gunicorn|uwsgi|lighttpd|nodejs|express|centos|ubuntu|debian|kubernetes|docker|helm|traefik|haproxy"
  ["email"]="smtp|imap|pop3|mailgun|sendgrid|postfix|exim|zimbra|exchange|roundcube|webmail"
  ["monitoring"]="prometheus|grafana|zabbix|splunk|datadog|new relic|appdynamics|kibana|elk stack|fluentd|graylog"
  ["wiki"]="mediawiki|tiki wiki|twiki|xwiki|dokuwiki"
)

for category in "${!cms_patterns[@]}"; do
  echo "$input" | grep -Ei "${cms_patterns[$category]}" | notify -id "$category" -bulk -d 4 -silent
done
