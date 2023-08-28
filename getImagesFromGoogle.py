import requests
from serpapi import GoogleSearch

api_key = "c9037e4b82470008621ea615f878af834c9695bd2c23765270fe5a279aa835ee"

# Create a GoogleSearch object
search = GoogleSearch({
    "q": "petechiae mouth roof",                                                          # Your search query
    "tbm": "isch",                                                                        # Specify you are doing image search
    "api_key": "c9037e4b82470008621ea615f878af834c9695bd2c23765270fe5a279aa835ee"         # Your SerpApi API key
})

# Execute the search and get the results
results = search.get_dict()

output_folder = "image_results/"

# Loop through image results
for idx, result in enumerate(results['images_results']):
    if idx >= 90:
        try:
            image_url = result['original']
        except (KeyError, ValueError):
            continue
        
        # Get the image data
        image_response = requests.get(image_url)
        
        # Generate a filename
        image_filename = f"image_{idx+1}.jpg"
        
        # Save the image locally
        with open(output_folder + image_filename, "wb") as image_file:
            image_file.write(image_response.content)
    else:
        print("Couldnt get more than 90 images, so cant download any more images")

print(f"Images downloaded and saved to {output_folder}")

"""
#This is for downloading search results and writing into a json file
 

# Specify the file name
output_file = "search_results.json"

# Write the results to a JSON file
with open(output_file, "w") as file:
    file.write(str(results))

# Print the search results
print(f"search results written to {output_file}")
"""

"""
def serpapi_get_google_images():
    image_results = []
    
    for query in ["Coffee", "boat", "skyrim", "minecraft"]:
        # search query parameters
        params = {
            "engine": "google",               # search engine. Google, Bing, Yahoo, Naver, Baidu...
            "q": query,                       # search query
            "tbm": "isch",                    # image results
            "num": "100",                     # number of images per page
            "ijn": 0,                         # page number: 0 -> first page, 1 -> second...
            "api_key": "...",                 # https://serpapi.com/manage-api-key
            # other query parameters: hl (lang), gl (country), etc  
        }
    
        search = GoogleSearch(params)         # where data extraction happens
    
        images_is_present = True
        while images_is_present:
            results = search.get_dict()       # JSON -> Python dictionary
    
            # checks for "Google hasn't returned any results for this query."
            if "error" not in results:
                for image in results["images_results"]:
                    if image["original"] not in image_results:
                        image_results.append(image["original"])
                
                # update to the next page
                params["ijn"] += 1
            else:
                print(results["error"])
                images_is_present = False
    
    # -----------------------
    # Downloading images

    for index, image in enumerate(results["images_results"], start=1):
        print(f"Downloading {index} image...")
        
        opener=urllib.request.build_opener()
        opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36")]
        urllib.request.install_opener(opener)

        urllib.request.urlretrieve(image["original"], f"SerpApi_Images/original_size_img_{index}.jpg")

    print(json.dumps(image_results, indent=2))
    print(len(image_results))

    """
