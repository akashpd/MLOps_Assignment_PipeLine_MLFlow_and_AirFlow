# You can create more variables according to your project. The following are the basic variables that have been provided to you
#DB_PATH = './home/Assignment/01_data_pipeline/scripts/'
DB_PATH = '/home/dags/Lead_scoring_data_pipeline/'
DB_FILE_NAME = 'lead_scoring_data_cleaning.db'
UNIT_TEST_DB_FILE_NAME = ''
DATA_DIRECTORY = '/home/dags/Lead_scoring_data_pipeline/data/' #'./data/'
LEAD_SCORING_FILE = 'leadscoring_inference' #changes done as inference pipeline 11 point #'leadscoring' #.csv file
INTERACTION_MAPPING = '/home/dags/Lead_scoring_data_pipeline/mapping/'
#INDEX_COLUMNS_TRAINING = ['created_date', 'city_tier', 'first_platform_c','first_utm_medium_c', #'first_utm_source_c','total_leads_droppped','referred_lead', 'app_complete_flag']

#After making change for inference, directly using this variable, #changes done as inference pipeline 11 point
INDEX_COLUMNS_TRAINING = ['created_date', 'city_tier', 'first_platform_c','first_utm_medium_c', 'first_utm_source_c','total_leads_droppped','referred_lead']


INDEX_COLUMNS_INFERENCE = []
NOT_FEATURES = []




