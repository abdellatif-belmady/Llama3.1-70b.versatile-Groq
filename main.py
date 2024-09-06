import streamlit as st
from langchain_community.document_loaders import WebBaseLoader


from chains import MoroccanCuisineGenerator


def create_streamlit_app(generator):
    st.title("🇲🇦 Moroccan Cuisine Recipe Generator and Cultural Insight Tool")
    
    st.sidebar.header("Options")
    option = st.sidebar.radio("Choose an option:", ("Generate Recipe", "Get Cultural Insights"))

    if option == "Generate Recipe":
        dish_name = st.text_input("Enter the name of a Moroccan dish:")
        dietary_restrictions = st.multiselect("Select any dietary restrictions:", 
                                              ["Vegetarian", "Vegan", "Gluten-free", "Nut-free", "Halal"])
        
        if st.button("Generate Recipe"):
            try:
                recipe = generator.generate_recipe(dish_name, ", ".join(dietary_restrictions))
                
                st.subheader(f"Recipe for {dish_name}")
                st.json(recipe)
                
                # Display recipe details in a more readable format
                st.subheader("Ingredients")
                for ingredient in recipe["Ingredients"]:
                    st.write(f"- {ingredient}")
                
                st.subheader("Cooking Instructions")
                for i, step in enumerate(recipe["Cooking instructions"], 1):
                    st.write(f"{i}. {step}")
                
                st.subheader("Additional Information")
                st.write(f"Cooking Time: {recipe['Cooking time']}")
                st.write(f"Difficulty Level: {recipe['difficulty level']}")
                
                st.subheader("Cultural Significance and History")
                st.write(recipe["Cultural significance and history"])
                
                st.subheader("Serving Suggestions")
                st.write(recipe["Serving suggestions and traditional accompaniments"])
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    elif option == "Get Cultural Insights":
        subject = st.text_input("Enter a Moroccan ingredient or cooking technique:")
        
        if st.button("Get Insights"):
            try:
                insights = generator.get_cultural_insights(subject)
                st.subheader(f"Cultural Insights: {subject}")
                st.write(insights)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    generator = MoroccanCuisineGenerator()
    st.set_page_config(layout="wide", page_title="Moroccan Cuisine Generator", page_icon="🇲🇦")
    create_streamlit_app(generator)

