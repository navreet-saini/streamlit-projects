import streamlit as st
import wikipedia 


st.title(" ⚛ My ChatBOT")

if "chat_history" not in st.session_state:         #create session state
    st.session_state.chat_history=[]    #to save messages



def get_response(user_input):               #this function gives response
    lower_inp=user_input.lower()

    if "how are you" in lower_inp:
        return "Am good! thankyou for asking.."
    elif "who build you" in lower_inp:
        return "Bot AI"
    else:
        try:
            answer=wikipedia.summary(lower_inp,sentences=2)
            return answer 
        except Exception:
            return "something went wrong"


user_input = st.chat_input("How Can I Help You?")

if user_input:
    st.session_state.chat_history.append(("🙍🏻‍♂️", user_input))   #we use tuple beaciuse we use indexes

    responses = get_response(user_input)
    st.session_state.chat_history.append(("🤖", responses))

for key,data in st.session_state.chat_history:
    # st.write(f"{key} : {data}")
    with st.chat_message(key):
        st.markdown(data)