import streamlit as st
from PIL import Image
import fitz 
import io
import os
from transformers import CLIPProcessor, CLIPModel
CLIPProcessor.safety_checker = None

def main():
    st.title("Hello, world!")

if __name__ == "__main__":
    main()
