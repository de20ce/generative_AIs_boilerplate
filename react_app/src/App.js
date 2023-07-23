import React, { useState, useEffect } from 'react'
import './App.css'
// yarn add @chatscope/chat-ui-kit-react
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import { MainContainer, ChatContainer, MessageList, Message, MessageInput, TypingIndicator } from '@chatscope/chat-ui-kit-react';
//import { w3cwebsocket as W3 } from "websocket";



function App() {
  const [messages, setMessages] = useState([
    {
      message: "Hello, I'm BotChat! Ask me anything!",
      sentTime: "now",
      sender: "BotChat"
    }
  ]);
  const [isTyping, setIsTyping] = useState(false);

  const client = new WebSocket('ws://0.0.0.0:8000/ws/chatbot/'); 
  //const client = new W3('ws://0.0.0.0:8000/ws/chatbot/'); 

 

  useEffect(() => { 
    client.onopen = () => {
      console.log("WebSocket Client Connected");
    };
    //client.onmessage = (message) => {
    //  console.log("In processMessage event", "Hi again")
    //};
  
  },[]);

  const handleSend = async (message) => {
    const newMessage = {
      message,
      direction: 'outgoing',
      sender: "user"
    };
    client.send(
      JSON.stringify({
        text: message,
      })
    );

    const newMessages = [...messages, newMessage];
    
    setMessages(newMessages);

    // Initial system message to determine BotChat functionality
    // How it responds, how it talks, etc.
    setIsTyping(true);
    await processMessageToBotChat(newMessages);
  };

  async function processMessageToBotChat(chatMessages) { // messages is an array of messages
    // Format messages for BotChat API
    // API is expecting objects in format of { role: "user" or "assistant", "content": "message here"}
    // So we need to reformat
    console.log("In processMessage", "Hi again")
    client.onmessage = (message) => {
      console.log("In processMessage event", "Hi again")
      if(message.data!==null){
      const dataFromServer = JSON.parse(message.data);
      console.log("Getting... ", dataFromServer['text']//['0']['msg']
      )
        
      if (dataFromServer['text']['0']!==null && typeof dataFromServer['text']['0']!=="undefined") {
      console.log("In the dataFromServer", dataFromServer)
       
        setMessages([...chatMessages, {
          message: dataFromServer['text']['0']['msg'], // dataFromServer['text']['0']['msg']
          sender: "BotChat"
      }]);
      
    }
  }
    else {
      console.log("hello no data receive from the server")
    }
    
  } 
  setIsTyping(false);
}

  return (
    <div className="App" style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
  }}>
      <div style={{ position:"relative", height: "800px", width: "700px"  }}>
      <h1>Generative BotChat</h1>
        <MainContainer >
          <ChatContainer>       
            <MessageList 
              scrollBehavior="smooth" 
              typingIndicator={isTyping ? <TypingIndicator content="BotChat is typing" /> : null}
            >
              {messages.map((message, i) => {
                console.log(message)
                return <Message key={i} model={message} />
              })}
            </MessageList>
            <MessageInput placeholder="Type message here" onSend={handleSend} />        
          </ChatContainer>
        </MainContainer>
      </div>
    </div>
  )
}

export default App