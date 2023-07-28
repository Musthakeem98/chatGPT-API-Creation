import openai

openai.api_key = "Your_ID"

Target_Audience = "Fashion-conscious millennials aged 25-35, primarily located in urban areas. They are interested in sustainable fashion and value unique and trendy designs"
Product_Details = "We offer handmade, eco-friendly clothing using organic materials. Our brand focuses on promoting ethical fashion and supporting local artisans."
Platform = "Instagram"
Content_Format = " Captions"
Key_Messages = "Emphasize our commitment to sustainable fashion, showcase the craftsmanship of our garments, and encourage followers to make conscious fashion choices"
Style = "Informative yet inspiring, with a touch of creativity and authenticity."

# Fix the messages variable assignment with the correct role for the AI response
messages = [
    {"role": "user", "content": "out target audience is " + Target_Audience + "."},
    {"role": "assistant", "content": Product_Details + " for " + Platform + Content_Format},
    {"role": "user", "content": "The Keymassage need to cover is " + Key_Messages + " and it's need to be " + Style + ". Give me the top 3 captions"}
]

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
print(completion.choices[0].message["content"])
