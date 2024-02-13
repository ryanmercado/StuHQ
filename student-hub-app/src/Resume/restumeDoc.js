import React, { Component } from 'react'
import './restumeDoc.css';

class restumeDoc extends Component {
  constructor(props) {
    super(props)
    this.state = {
      school: '',
      major:'',
      experience: '',
      skills: []
    }
  }

  handleInputChange = (e) => {
    this.setState({ [e.target.name]: e.target.value })
  }

  addSkill = () => {
    this.setState({ 
      skills: [...this.state.skills, this.state.currentSkill], 
      currentSkill: '' 
    })
  }

  removeSkill = (indexToRemove) => {
    this.setState({ 
      skills: this.state.skills.filter((_, index) => index !== indexToRemove) 
    })
  }

  render() {
    const { experience, school, major, skills, currentSkill } = this.state
    return (
      <div>
        <label>Experience:</label>
        <input 
          name='experience' 
          value={experience} 
          onChange={this.handleInputChange} 
          placeholder='Enter your work experience' 
          />
        <label>School:</label>
        <input 
          name='school' 
          value={school} 
          onChange={this.handleInputChange} 
          placeholder='Enter your education details' 
          />
        <label>Major:</label>
        <input 
          name='major' 
          value={major} 
          onChange={this.handleInputChange} 
          placeholder='Enter your major' 
          />
        <label>Skills:</label>
        { skills.map((skill, index) => (
          <div key={index}>
            {skill}
            <button onClick={() => this.removeSkill(index)}>Remove</button>
          </div>
        ))}
        <input 
          value={currentSkill} 
          onChange={e => this.setState({ currentSkill: e.target.value })} 
        />
        <button onClick={this.addSkill} >Add Skill</button>
      </div>
    )
  }
}

export default restumeDoc;