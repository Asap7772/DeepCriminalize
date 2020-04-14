import React from "react";
import {Table, Image, Row, Col} from "react-bootstrap";
import $ from "jquery";
class Output extends React.Component {
  constructor(props) {
    super(props);
  }

  /* Sample code for stopping updates.
  shouldComponentUpdate(nextProps, nextState) {
    if (this.props.count !== nextProps.count) {
      return true;
    } else {
      return false;
    }
  }

  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/get-the-cube-edge/index.php", true);
  xhttp.setRequestHeader("content-type", "application/json");
  xhttp.send(json);

  */
  make_requests(){
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = false;

    let data = this.props.json;

    xhr.addEventListener("readystatechange", function () {
      if (this.readyState === 4) {
        console.log(this.responseText);
        setTimeout(function () {
          var xh = new XMLHttpRequest();
          xh.withCredentials = false;
          console.log(data);
          xh.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
              console.log(JSON.parse(this.responseText));
            //  document.getElementById("ItemPreview").src = "data:image/png;base64," + this.responseText[0];
            console.log(this.responseText[0])
            var img = document.getElementById("ItemPreview")
            var img2 = document.getElementById("ItemPreview2")
            var img3 = document.getElementById("ItemPreview3")
            img.src = "data:image/png;base64, " + JSON.parse(this.responseText)[0]
            img2.src = "data:image/png;base64, " + JSON.parse(this.responseText)[1]
            img3.src = "data:image/png;base64, " + JSON.parse(this.responseText)[2]

            }
          });

          xh.open("POST", "http://deepcriminalize.ngrok.io");
          xh.setRequestHeader("Content-Type", "application/json");
          // xh.setRequestHeader("User-Agent", "PostmanRuntime/7.20.1");
          xh.setRequestHeader("Accept", "*/*");
          xh.setRequestHeader("Cache-Control", "no-cache");
          xh.setRequestHeader("Postman-Token", "1e67983e-fd86-43d5-984a-db27854e4368,6cb1f310-58d4-4e45-84fd-d3503b5571fc");
          // xh.setRequestHeader("Host", "deepcriminalize.ngrok.io");
          // xh.setRequestHeader("Accept-Encoding", "gzip, deflate");
          // xh.setRequestHeader("Content-Length", "187");
          // xh.setRequestHeader("Connection", "keep-alive");
          xh.setRequestHeader("cache-control", "no-cache");
          xh.setRequestHeader("dataType",'jsonp');
          xh.send(data);
        }, 100);
        //secondPost(data);
      }
    });

    xhr.open("PUT", "http://deepcriminalize.ngrok.io");
    xhr.setRequestHeader("Content-Type", "application/json");
    // xhr.setRequestHeader("User-Agent", "PostmanRuntime/7.20.1");
    xhr.setRequestHeader("Accept", "*/*");
    xhr.setRequestHeader("Cache-Control", "no-cache");
    xhr.setRequestHeader("Postman-Token", "17cc52ac-ab49-419f-96cd-e2473620cb1d,f4f9933c-c3cb-44cc-b4d1-e7b22cc8b47d");
    // xhr.setRequestHeader("Host", "deepcriminalize.ngrok.io");
    // xhr.setRequestHeader("Accept-Encoding", "gzip, deflate");
    // xhr.setRequestHeader("Content-Length", "185");
    // xhr.setRequestHeader("Connection", "keep-alive");
    xhr.setRequestHeader("cache-control", "no-cache");
    xhr.setRequestHeader("dataType",'jsonp');
    xhr.send(data);

  }

  render() {
    return (
      <Row style={{ paddingTop: 20, }}>
        <Col md="2" xl="2" lg="2" />
        <Col md="9" xl="9" lg="9">
        <p>{this.make_requests()}</p>

        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Image 1</th>
              <th>Image 2</th>
              <th>Image 3</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" id="ItemPreview" width="300px"/> </td>
              <td><img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" id = "ItemPreview2"  width="300px"/> </td>
              <td><img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" id = "ItemPreview3" width="300px"/> </td>
            </tr>
          </tbody>
        </Table>
      </Col>
      <Col md="2" xl="2" lg="2" />
    </Row>
    );
  }
}

export default Output;
