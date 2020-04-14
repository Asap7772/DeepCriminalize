import React from "react";
import {
  Row,
  Col,
  Form,
  Button,
  InputGroup
} from "react-bootstrap";
import './Form.css';
import FormValidator from "./FormValidator.js";
import SpeechRecognition from "./SpeechRecog.js";

export class InputForm extends React.Component {
  constructor(props) {
    super(props);
    this.validator = new FormValidator([
      {
        field: "witness_name",
        method: "isEmpty",
        validWhen: false,
        message: "Please enter a valid input."
      },
      {
        field: "case_number",
        method: "isEmpty",
        validWhen: false,
        message: "Please enter a valid input."
      },
      {
        field: "case_number",
        method: "isFloat",
        validWhen: true,
        message: "Please enter a valid input."
      },
      {
        field: "e",
        method: "equals",
        args: ["Choose"],
        validWhen: false,
        message: "Please enter select an option."
      },
      {
        field: "g",
        method: "equals",
        args: ["Choose"],
        validWhen: false,
        message: "Please enter select an option."
      }
    ]);

    this.state = {
      witness_name:"",
      case_number:"",
      e:"Choose",
      g:"Choose",
      md: "",
      validation: this.validator.valid(),
      display: false
    };
    this.inputch = this.inputch.bind(this);
    this.submit = this.submit.bind(this);
    this.submitted = false;
  }

  inputch(event){
    event.preventDefault();
    this.props.input(event)
    this.setState({
      [event.target.name]: event.target.value
    });
  };

  submit(event){
    event.preventDefault();
    const validation = this.validator.validate(this.state);
    this.setState({ validation });
    this.submitted = true;

    if (validation.isValid) {
      this.setState({ display: true});
      this.props.submit(event, true)
      this.submitted = false;
    }
  }

  render() {
    const val = this.submitted
      ? this.validator.validate(this.state)
      : this.state.validation;

    return (
      <div style={{ paddingTop: 20, paddingBottom: 15, background:"#FCFCFC"}}>
        <h1 align="center">Enter Case Details</h1>
        <Row style={{ paddingTop: 20, }}>
          <Col md="2" xl="2" lg="2" />
          <Col md="9" xl="9" lg="9" align="center">

            <Form>
              <Form.Group as={Row} align="center" controlId="formCaseNo">
                  <Form.Label >Case Number:</Form.Label>

                  <InputGroup>
                    <Form.Control
                      required
                      type="number"
                      placeholder="Case Number"
                      name="case_number"
                      onChange={this.inputch}
                      min={1}
                      step={1}
                    />
                  </InputGroup>
                  <span className="help-block" style={{ color: "red" }}>
                    {val.case_number.message}
                  </span>
              </Form.Group>

              <Form.Group as={Row} align="center" controlId="witnessName">

                  <Form.Label>Witness Name:</Form.Label>

                  <InputGroup>
                    <Form.Control
                      required
                      type="text"
                      placeholder="Witness Name"
                      defaultValue={""}
                      name="witness_name"
                      onChange={this.inputch}
                    />
                  </InputGroup>
                  <span className="help-block" style={{ color: "red" }}>
                    {val.witness_name.message}
                  </span>

              </Form.Group>

              <Form.Group as={Row} align="center" controlId="e">
                <Form.Label>Ethnicity</Form.Label>
                  <Form.Control as="select" name="e" onChange={this.inputch}>
                    <option>Choose</option>
                    <option value="asian">Asian</option>
                    <option value="hispanic">Hispanic</option>
                    <option value="caucasian">Caucasian</option>
                    <option value="indian">Indian</option>
                    <option value="african_american">African-American</option>
                  </Form.Control>
                  <span className="help-block" style={{ color: "red" }}>
                    {val.e.message}
                  </span>
              </Form.Group>

              <Form.Group as={Row} align="center" controlId="g">
                <Form.Label>Gender</Form.Label>
                  <Form.Control as="select" name="g" onChange={this.inputch}>
                    <option>Choose</option>
                    <option value="man">Male</option>
                    <option value="woman">Female</option>
                  </Form.Control>
                  <span className="help-block" style={{ color: "red" }}>
                    {val.g.message}
                  </span>
              </Form.Group>

              <Form.Group as={Row} align="center" controlId="witness">
                <Form.Label>Describe Witness
                </Form.Label>
              </Form.Group>
              <Row> <SpeechRecognition/></Row>

              <Form.Group as={Row}>
                <Col md={12} lg={10} xl={10} align="center">
                  <Button variant="primary" onClick={this.submit}>
                    Generate Images
                  </Button>
                </Col>
              </Form.Group>

            </Form>
          </Col>
          <Col md="2" lg="2" xl="2" />
        </Row>
      </div>
    );
  }
}
