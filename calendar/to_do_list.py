class ToDoList():
    todo = [] # contains all the events to be shown in list

    # Probably a flask end point 
    def addEvent(self, event):
        if(event.get("on_to_do_list", True)):
           self.todo.append(event)

    def get_todo_list(self):
        return self.todo



# Potential Flask configuration

# @app.route('/add_event', methods=['POST'])
# def add_event():
#     data = request.get_json()
#     todo_list.add_event(data)
#     return jsonify({'message': 'Event added successfully'})

# @app.route('/get_todo_list', methods=['GET'])
# def get_todo_list():
#     return jsonify({'todo_list': todo_list.events})

# if __name__ == '__main__':
#     app.run(debug=True)


