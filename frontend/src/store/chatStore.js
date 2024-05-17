import {create} from 'zustand';
import {devtools, persist} from 'zustand/middleware'

const chatStore = (set) => ({
    messages: [],
    addMessage: (message) => {
        set((state) => ({
            messages: [...state.messages, message],
        }))
    }
})

const useChatStore = create(
    devtools(
        persist(chatStore, {
            name: "messages",
        })
    )
)
export default useChatStore;