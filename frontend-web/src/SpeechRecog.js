import React, {
  Component
} from "react";
import {
  Button,
  Row,
  Col,
} from "react-bootstrap";
import PropTypes from "prop-types";
import SpeechRecognition from "react-speech-recognition";

const propTypes = {
  // Props injected by SpeechRecognition
  transcript: PropTypes.string,
  resetTranscript: PropTypes.func,
  startListening: PropTypes.func,
  stopListening: PropTypes.func,
  browserSupportsSpeechRecognition: PropTypes.bool,
};

const options = {
  autoStart: false,
  //  continuous: false
}


const Dictaphone = ({
  transcript,
  resetTranscript,
  startListening,
  stopListening,
  browserSupportsSpeechRecognition
}) => {
  if (!browserSupportsSpeechRecognition) {
    return null
  }

  function stoprec() {
    stopListening()
  }

  function startrec() {
    resetTranscript()
    startListening()
  }

  return (

    <div>
      <Row>
          <Button onClick = {startrec} style={{marginRight: 15, marginLeft: 15}}> Start </Button>
          <Button onClick = {stoprec} > Stop </Button>
      </Row>
      <Row>
      <div id="desc" style={{padding: 15, background: "white", border: "1px solid #d3d3d3", borderRadius: 5, marginTop: 15, marginBottom: 10, marginLeft: 15}}>
        <span> {transcript} </span>
      </div>
      </Row>
    </div>
  );
};

Dictaphone.propTypes = propTypes;

export default SpeechRecognition(options)(Dictaphone);
