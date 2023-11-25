import React from 'react'
import Link from 'next/link'
import NavBar from '@/app/components/navbar'
import Footer from '@/app/components/footer'
import PlayButton from '@/app/svgs/play'
import '@/app/styles/upload.css'

const upload = () => {
  return (
    <div>
        <NavBar />
        <div className="upload-container">
            <div className="video-side">
                <div className="actual-video"></div>
                <PlayButton />
            </div>
            <div className="image-side">
                <div className="no-image">No Images.</div>
                <form action="/">
                    <input className="label" type="text" name='Label' placeholder= "Label"/>
                    <input className="upload-image" type="submit" name='Upload Images' value="Upload Images"/>
                </form>
            </div>
        </div>
        <Footer />
    </div>
  )
}

export default upload
