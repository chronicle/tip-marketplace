INTEGRATION_NAME = "Anomali"

# ACTIONS NAMES
PING_SCRIPT_NAME = f"{INTEGRATION_NAME} - Ping"
GET_RELATED_ASSOCIATIONS_SCRIPT_NAME = f"{INTEGRATION_NAME} - Get Related Associations"
GET_THREAT_INFO_SCRIPT_NAME = f"{INTEGRATION_NAME} - GetThreatInfo"


EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

VULNERABILITY_ASSOCIATION_TYPE = 'vulnerability'
CAMPAIGN_ASSOCIATION_TYPE = 'campaign'
ACTOR_ASSOCIATION_TYPE = 'actor'
SIGNATURE_ASSOCIATION_TYPE = 'signature'

CVE_ENTITY_TYPE = "CVE"
CAMPAIGN_ENTITY_TYPE = "THREATCAMPAIGN"
ACTOR_ENTITY_TYPE = "THREATACTOR"
SIGNATURE_ENTITY_TYPE = "THREATSIGNATURE"

ENTITY_CREATING_VALID_VALUES_MAPPER = [
    VULNERABILITY_ASSOCIATION_TYPE,
    CAMPAIGN_ASSOCIATION_TYPE,
    ACTOR_ASSOCIATION_TYPE,
    SIGNATURE_ASSOCIATION_TYPE
]


ASSOCIATION_TYPE_TO_ENTITY = {
    VULNERABILITY_ASSOCIATION_TYPE: CVE_ENTITY_TYPE,
    CAMPAIGN_ASSOCIATION_TYPE: CAMPAIGN_ENTITY_TYPE,
    ACTOR_ASSOCIATION_TYPE: ACTOR_ENTITY_TYPE,
    SIGNATURE_ASSOCIATION_TYPE: SIGNATURE_ENTITY_TYPE
}

# ADDITIONAL ENTITY TYPES
EMAIL_TYPE = 101

# TABLES NAMES
ASSOCIATIONS_TABLE_NAME = "Related Associations"
# The max length of a association's description, splitted with spaces
MAX_LENGTH_FOR_JSON_RESULT_STRING = 150


# MAPPINGS
SEVERITY_MAPPING = {
    'low': 1,
    'medium': 2,
    'high': 3,
    'very high': 4,
    'very-high': 4,
}
