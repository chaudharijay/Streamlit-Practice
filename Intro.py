import streamlit as st

#header and title

st.title("This is title tag")
st.header("this is header tag")
st.subheader("this is subheader tag")
st.text("this is a text tag")

#markdown - (https://markdownguide.offshoot.io/cheat-sheet/)
st.markdown("this is markdown function")
st.markdown("**this is bold markdown function**")
st.markdown("*this is italic markdown function*")
st.markdown("***this is bold and italic markdown function***")
st.markdown("# hello world")
st.markdown("> hello world")
st.markdown("---")

# ordered list 
st.markdown("1. first")
st.markdown("2. second")
st.markdown("3. third")

# un - ordered list 
st.markdown("- first")
st.markdown("- second")
st.markdown("- third")

# code
st.markdown("`this for code`")

# link
st.markdown("[title]{https://www.example.com}")


st.caption("this is a caption")

# for matrix (https://katex.org/docs/supported)
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") 

json={"a":"1,2,3", "b":"4,5,6"}
st.json(json)

code='''print("this is a print function")'''
st.code(code)
st.code(code, language="python")

st.write()



