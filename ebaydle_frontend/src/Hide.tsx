import React, { useState } from 'react';

export default function ToggleDiv() {
  const [isVisible, setIsVisible] = useState(false);

  function handleClick() {
    setIsVisible(!isVisible);
  }

  return (
    <div>
      <button onClick={handleClick}>Toggle Div</button>
      {isVisible && <div>This div is now visible.</div>}
    </div>
  );
}

/*
import React, { useState } from 'react'

function ToggleDiv() {
  const [isVisible, setIsVisible] = useState(false)

  function handleClick() {
    setIsVisible(!isVisible)
  }

  return (
    <div>
      <button onClick={handleClick}>Toggle Div</button>
      {isVisible && <div>This div is now visible.</div>}
    </div>
  )
}
*/
