import React, { useState } from 'react';
import { LuSendHorizonal } from "react-icons/lu";
import useChatStore from '../store/chatStore';
import axios from 'axios';

const InputBox = () => {
    const [question, setQuestion] = useState("");
    const addMessage = useChatStore((state) => state.addMessage)
    const replaceLastMessage = useChatStore((state) => state.replaceLastMessage)

    const handleSendMessage = async () => {
        addMessage(question);
        try{
            addMessage("Genearating...")
            const response = await axios.post('http://localhost:8000/chat', { "question": question});
            replaceLastMessage(response.data.response["content"]);
        } catch (error) {
            console.error('Error uploading file:', error);
        }
        setQuestion("");
    }

    return (
        <div className='fixed bottom-0 sm:left-20 sm:right-20 m-5 bg-white py-2 px-4 flex border-2 border-black rounded'>
            <input className='w-full focus:outline-none' type="text" placeholder='Send a message...' value={question} 
            onChange={(e)=>{
                setQuestion(e.target.value);
            }}/>
            <LuSendHorizonal className='my-auto' onClick={handleSendMessage} />
        </div>
    )
}

export default InputBox