#!/bin/bash

if [ -t 0 ]; then
  echo "Usage: cat input | $0"
  exit 1
fi

input=$(cat)

declare -A cms_patterns=(
  ["wordpress"]="wordpress|wp|powered by wordpress"
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
)

for category in "${!cms_patterns[@]}"; do
  echo "$input" | grep -Ei "${cms_patterns[$category]}" | notify -id "$category" -bulk -d 2
done
