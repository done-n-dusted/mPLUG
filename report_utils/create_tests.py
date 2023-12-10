import json
import matplotlib.pyplot as plt
import random
from PIL import Image
import sys

json_file_path = sys.argv[1]

with open(json_file_path, 'r') as file:
    data = json.load(file)

# random_images = random.sample(data, 2)  # Change 5 to the desired number of images
ct = 5
# print(random_images)
# Display each image and its caption
for image_data in data:
    if ct == 0:
        break
    # try:
    print("taking image_id", image_data['question_id'])
    image_id = image_data['question_id']
    caption = image_data['pred_caption']
    # /home/paperspace/Desktop/data/test2014_img
    # Load and display the image using matplotlib (replace this with your image loading/display logic)
    img = Image.open('/home/paperspace/Desktop/data/val2014_img/' + image_id)
    plt.imshow(img)
    plt.title(caption)
    plt.axis('off')  # Hide axes
    # plt.show()
    plt.savefig('results/' + image_id, bbox_inches='tight')
    print("Done for ", image_id)
    ct -= 1
    # except:
        # print("passing on", image_data['question_id'])

