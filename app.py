import streamlit as st
import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path


# this is for saving images and prediction
def save_image(uploaded_file):
    try:
        if uploaded_file is not None:
            save_path = os.path.join("images", "input.jpeg")
            with open(save_path, "wb") as f:
                f.write(uploaded_file.read())
            st.success(f"Image saved to {save_path}")

            # Load the model
            model = torch.load(Path('model/model.pt'))
            model.eval()  # Set the model to evaluation mode

            # Define the image transformations
            trans = transforms.Compose([
                transforms.Resize(224),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
            ])

            # Open the image
            image = Image.open(save_path).convert("RGB")

            # Apply transformations
            input_tensor = trans(image)
            input_tensor = input_tensor.unsqueeze(0)  # Add batch dimension

            # Perform the prediction
            with torch.no_grad():
                output = model(input_tensor)

            # Get the prediction
            prediction = int(torch.max(output.data, 1)[1].numpy())

            # Display the prediction
            if prediction == 0:
                st.text_area(label="Prediction:", value="Normal", height=100)
            elif prediction == 1:
                st.text_area(label="Prediction:", value="PNEUMONIA", height=100)
            else:
                st.text_area(label="Prediction:", value="Unknown", height=100)
        else:
            st.warning("Please upload an image file.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    st.title("Xray lung classifier")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    save_image(uploaded_file)


    