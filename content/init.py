# ------ COURSE PARAMS ------
#course_id = '\S*deeplearning\S*'
github_repo = 'leonidasf300/dl22_2'
#endpoint = 'https://m5knaekxo6.execute-api.us-west-2.amazonaws.com/dev-v0001/rlxmooc'
# ------ COURSE PARAMS ------

zip_file_url ="https://github.com/%s/archive/main.zip"%github_repo
print(zip_file_url)

def init(force_download=False):
    print(zip_file_url)

'''
def init(force_download=False):
    from IPython.display import display, HTML
    js = """
<meta name="google-signin-client_id"
      content="461673936472-kdjosv61up3ac1ajeuq6qqu72upilmls.apps.googleusercontent.com"/>
<script src="https://apis.google.com/js/client:platform.js?onload=google_button_start"></script>
    """

    display(HTML(js))

    if force_download or not os.path.exists("local"):
        print("replicating local resources")
        dirname = github_repo.split("/")[-1]+"-main/"
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        if os.path.exists("local"):
            shutil.rmtree("local")
        if os.path.exists(dirname+"/content/local"):
            shutil.move(dirname+"/content/local", "local")
        elif os.path.exists(dirname+"/local"):
            shutil.move(dirname+"/local", "local")
        shutil.rmtree(dirname)
 '''       
import requests, zipfile, io, os, shutil, subprocess 
