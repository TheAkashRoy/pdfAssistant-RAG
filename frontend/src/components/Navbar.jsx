import React, { useState } from 'react';
import { CgAdd } from 'react-icons/cg';
import { CiFileOn } from 'react-icons/ci';
import axios from 'axios'; // Make sure to install the 'axios' library

const Navbar = () => {
  const [file, setFile] = useState(null);

  const handleClick = () => {
    // Open the file picker dialog
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.pdf';
    fileInput.onchange = (event) => {
      const selectedFile = event.target.files[0];
      setFile(selectedFile);
      uploadFile(selectedFile);
    };
    fileInput.click();
  };

  const uploadFile = async (file) => {
    try {
      const formData = new FormData();
      formData.append('pdf', file);
      console.log(formData);

      // Replace 'your-backend-endpoint' with the actual endpoint URL
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      console.log('File uploaded successfully:', response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div className="flex justify-around sm:justify-between sm:px-20 py-2 bg-[#FEFEFF] shadow-lg">
      <div className="text-xl my-auto">pdfAssitance</div>

      <div className="flex ">
        {file && (
          <div className="flex rounded-xl mr-1 sm:mr-5">
            <div className="m-auto border-black border p-2 rounded">
              <CiFileOn />
            </div>
            <div className="m-auto mx-2 py-3 sm:mx-3">{file.name}</div>
          </div>
        )}

        <button
          className="flex px-3 border-black border-2 rounded-xl"
          onClick={handleClick}
        >
          <div className="m-auto">
            <CgAdd />
          </div>
          <div className="m-auto mx-3 py-3 hidden sm:block">Upload PDF</div>
        </button>
      </div>
    </div>
  );
};

export default Navbar;