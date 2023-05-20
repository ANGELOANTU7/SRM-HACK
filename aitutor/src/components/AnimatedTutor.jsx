import React, { useState, useEffect } from 'react';
import '../AnimatedTutor.css';
import image from '../assets/head.png'

const AnimatedTutor = ({ script }) => {
    const [isSpeaking, setIsSpeaking] = useState(false);
    useEffect(() => {
      if (isSpeaking) {
        const utterance = new SpeechSynthesisUtterance(script);
        speechSynthesis.speak(utterance);
      } else {
        speechSynthesis.cancel();
      }
    }, [isSpeaking, script]);
  const speakText = () => {
    setIsSpeaking(true);
  };

  const stopSpeaking = () => {
    setIsSpeaking(false);
  };

  return (
    <div className="animated-tutor-container">
      <div className={`animated-tutor ${isSpeaking ? 'is-speaking' : ''}`}>
        <img
          src={isSpeaking ? 'https://www.reallusion.com/cartoon-animator/includes/images/features/2D%20Talking%20head/old%202D%20talking%20head.gif' : image}
          alt="Animated Tutor"
          className="tutor-avatar"
        />
        <div className="tutor-message">{script}</div>
        <div className="tutor-controls">
          {!isSpeaking && (
            <button onClick={speakText}>Start</button>
          )}
          {isSpeaking && (
            <button onClick={stopSpeaking}>Stop</button>
          )}
        </div>
      </div>
    </div>
  );
};

export default AnimatedTutor;

