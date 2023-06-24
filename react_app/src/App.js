import React, { useState } from 'react'
import './App.css';

export default function App() {
  const [id, setId] = useState(1)
  const [messageList, setMessageList] = useState([{ id: 0, message: 'Salut!', fromUser: false }])
  const [userMessage, setUserMessage] = useState('')

  function handleClick() {
    const newUserMessage = { id: id, message: userMessage, fromUser: true}
    const newBotMessage = { id: `${id+1}`, message: 'Je suis bête', fromUser: false}
    setMessageList([...messageList, newUserMessage, newBotMessage])
    setUserMessage('')
    setId(id + 2)
  }

  return <div className='app'>
    <div className='container'>
      {
        messageList.map(({id, message, fromUser}) => <Message key={id} message={message} fromUser={fromUser}/>)
      }
    </div>
    <textarea value={userMessage} onChange={(e) => setUserMessage(e.target.value)} rows={3} placeholder='Envoyer un message' autoFocus/>
    <button onClick={handleClick} disabled={userMessage === ''}>Envoyer</button>
  </div>
};

function Message({ message, fromUser }) {
  return <div className={fromUser ? 'message-from-user' : 'message-from-bot'}>
    <p>{message}</p>
  </div>
}
