import React from 'react'
import AnimatedTutor from './AnimatedTutor';

function Tutor() {
    const dummyScript = "Hi my name is Harshed.";
  return (
    <div>
         <AnimatedTutor script={dummyScript} />
    </div>
  )
}

export default Tutor