import React from 'react'
import InputBox from './InputBox'
import MessagesBox from './MessagesBox'

const ChatWindow = () => {
  return (
    <>
        <div className="flex flex-col  mx-6 sm:mx-20 rounded">
            <MessagesBox />
            <InputBox />
        </div>
        
    </>
  )
}

export default ChatWindow