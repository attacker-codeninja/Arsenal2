## Setup

```curl -s https://raw.githubusercontent.com/Vulnpire/Arsenal/refs/heads/c2/scripts/web/basic/cms_detect/cms_detect.sh > /tmp/cms_detect.sh && chmod +x /tmp/cms_detect.sh && sudo mv /tmp/cms_detect.sh /usr/local/bin/```

Detects a wide range of CMS platforms, including:

    WordPress
    Jira/Atlassian
    Drupal
    Joomla
    E-Commerce CMS (e.g., Magento, Shopify, WooCommerce)
    Forums and Community Platforms (e.g., phpBB, vBulletin, XenForo)
    Educational Platforms (e.g., Moodle, Blackboard)
    Static Site CMS (e.g., Jekyll, Hugo)
    Enterprise CMS (e.g., Sitecore, AEM)
    And many more!

The script currently contains 211 individual patterns across 34 categories.

## Categories and Pattern Counts

| **Category**            | **Patterns** | **Examples**                                    |
|--------------------------|--------------|------------------------------------------------|
| **CMS Platforms**        | 4            | WordPress, Drupal                              |
| **Jira/Atlassian Tools** | 5            | Jira, Confluence                              |
| **E-Commerce CMS**       | 10           | Magento, Shopify, WooCommerce                 |
| **General CMS**          | 19           | TYPO3, Ghost, Sitefinity                      |
| **Forums**               | 7            | phpBB, XenForo, vBulletin                     |
| **Education Platforms**  | 5            | Moodle, Blackboard                            |
| **Portals**              | 11           | Liferay, Webflow                              |
| **PHP Frameworks**       | 8            | Laravel, CodeIgniter, Symfony                 |
| **Wiki Platforms**       | 5            | MediaWiki, DokuWiki                           |
| **Static Site CMS**      | 5            | Jekyll, Hugo, Gatsby                          |
| **Government Platforms** | 3            | OpenPublic, CivicSpace                        |
| **Enterprise CMS**       | 7            | Sitecore, Adobe Experience Manager (AEM)      |
| **Servers**              | 8            | Apache, Nginx, IIS                            |
| **Admin Panels**         | 14           | Admin, Backend, Dashboard                     |
| **Sensitive Subdomains** | **30**       | Staging, QA, Dev, Backup, Auth, Billing       |
| **Open Directories**     | 7            | Index of, Directory Listing                   |
| **API Endpoints**        | 8            | REST API, GraphQL, OpenAPI                    |
| **Cloud Services**       | 9            | AWS, Google Cloud, Heroku                     |
| **Setup and Configuration** | 12       | Setup, Installation, Onboarding               |
| **Titles and Indicators**| 12           | Powered by, Login Page, Dashboard             |
| **Frameworks**           | 10           | Django, React, Angular, Flask                 |
| **Database Systems**     | 9            | MySQL, PostgreSQL, MongoDB                    |
| **Technologies**         | 12           | Kubernetes, Docker, HAProxy                   |
| **Email Services**       | 10           | Mailgun, Sendgrid, Zimbra                     |
| **Monitoring Tools**     | 9            | Prometheus, Grafana, Splunk                   |

---

- More to be added!

## Highlights

### **Sensitive Subdomains**
The script targets **30 subdomains**, including high-value ones such as:
- **Development/Testing**: staging, dev, test, qa, sandbox
- **Infrastructure**: vpn, api, storage, backup
- **Authentication**: auth, login, identity, secure
- **Financial**: billing, payments, invoice

### **E-Commerce and APIs**
Supports detection for modern platforms like Magento, Shopify, and WooCommerce, as well as REST, GraphQL, and SOAP APIs.

---
