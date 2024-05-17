import React from 'react'
import { CgAdd } from "react-icons/cg";
import { CiFileOn } from "react-icons/ci";

const Navbar = () => {
  return (
    <div className='flex justify-around sm:justify-between sm:px-20 py-2 bg-[#FEFEFF] shadow-lg'>
        <div className='text-xl my-auto'> pdfAssitance </div>

        <div className='flex '>
        <div className='flex rounded-xl mr-1 sm:mr-5'>
            <div className='m-auto border-black border p-2 rounded' > <CiFileOn /> </div>
            <div className='m-auto mx-2 py-3 sm:mx-3'> pdfname.pdf</div>
        </div>

        <button className='flex px-3 border-black border-2 rounded-xl'>
            <div className='m-auto' > <CgAdd /> </div>
            <div className='m-auto mx-3 py-3 hidden sm:block'> Upload PDF</div>
        </button>
        </div>
    </div>
  )
}

export default Navbar