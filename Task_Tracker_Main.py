import argparse
from Task_Tracker_Functions import add_task, update_task, delete_task,mark_in_progress,mark_done, list_tasks

parser = argparse.ArgumentParser(description="Task Tracker CLI")

subparsers = parser.add_subparsers(dest="operation",required=True,help="Operation to do")

add_parser = subparsers.add_parser("add", help="Add some task")
add_parser.add_argument("description",type=str, help="Description to your new task")

update_parser = subparsers.add_parser("update",help="Update some task")
update_parser.add_argument("id",type=int,help="Id of the task to update")
update_parser.add_argument("new_description",type=str,help="New description for the task")

delete_parser = subparsers.add_parser("delete", help="Delete some task")
delete_parser.add_argument("id",type=int,help="Id of the task to delete")

mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark some task to in-progress")
mark_in_progress_parser.add_argument("id", type=int,help="Id of the task to make in progress")

mark_in_progress_parser = subparsers.add_parser("mark-done", help="Mark some task to done")
mark_in_progress_parser.add_argument("id", type=int,help="Id of the task to make in done")

list_parser = subparsers.add_parser("list", help="List all tasks")
list_subparsers = list_parser.add_subparsers(dest="list_command",help="List Subparsers")

in_progress_list_parser = list_subparsers.add_parser("done",help="List of tasks completed") 
in_progress_list_parser = list_subparsers.add_parser("todo",help="List of tasks to do") 
in_progress_list_parser = list_subparsers.add_parser("in-progress",help="List of tasks in progress") 


args = parser.parse_args()

if args.operation == "add":
    add_task(args.description)

elif args.operation == "update":
    update_task(args.id,args.new_description)

elif args.operation == "delete":
    delete_task(args.id)

elif args.operation == "mark-in-progress":
    mark_in_progress(args.id)

elif args.operation == "mark-done":
    mark_done(args.id)

elif args.operation == "list":
    if args.list_command:
        list_tasks(args.list_command)
    else:
        list_tasks()
        