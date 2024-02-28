import React, { Component } from 'react';

// Each Component is just an input field for simplicity.
// In reality, you would have your own fields and logic
class GeneralInfo extends Component {
  state = { info: '' };

  handleInputChange = (e) => this.setState({ info: e.target.value });

  next = () => {
    this.props.onStateChange('generalInfo', this.state.info);
    this.props.nextStep();
  }

  render(){
    return (
      <div>
        <input type="text" value={this.state.info} onChange={this.handleInputChange} placeholder="General Info" />
        <button onClick={this.next}>Next</button>
      </div>
    )
  }
}

class SkillsList extends Component {
  state = { skills: '' };

  handleInputChange = (e) => this.setState({ skills: e.target.value });

  next = () => {
    this.props.onStateChange('skillsList', this.state.skills);
    this.props.nextStep();
  }

  render(){
    return (
      <div>
        <input type="text" value={this.state.skills} onChange={this.handleInputChange} placeholder="Skills" />
        <button onClick={this.next}>Next</button>
      </div>
    )
  }
}

// Definition for JobsList, ProjectExperience, ExtracurricularActivities, LifeObjective, RelevantCourseworkList, VolunteerWork, AwardsList here...
// For demo purposes we've only do GeneralInfo and SkillsList

class ResumeDoc extends Component {
  state = {
    step: 1,
    generalInfo: '',
    skillsList: '',
    // Define fields for other components here...
  }

  nextStep = () => this.setState(prevState => ({ step: prevState.step + 1 }));

  onStateChange = (field, value) => this.setState({ [field]: value });

  render() {
    switch(this.state.step) {
      case 1:
        return <GeneralInfo nextStep={this.nextStep} onStateChange={this.onStateChange} />;
      case 2:
        return <SkillsList nextStep={this.nextStep} onStateChange={this.onStateChange} />;
      case 3: 
        return <JobsList nextStep={this.nextStep} onStateChange={this.onStateChange} />;
      // Add cases for other components here...
      default:
        return <button onClick={() => console.log(this.state)}>Submit</button>;
    }
  }
}

export default ResumeDoc;