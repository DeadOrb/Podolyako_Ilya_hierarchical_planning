(define (domain robot)
  (:requirements :hierarchical)
  (:types package room door)
  (:predicates
        (armempty)
        (rloc ?loc - room)
        (in ?obj - package ?loc - room)
        (holding ?obj - package)
        (closed ?d - door)
        (door ?loc1 - room ?loc2 - room ?d - door)
)

(:action pickup
        :parameters (?obj - package ?loc - room)
        :precondition (and (armempty) (rloc ?loc) (in ?obj ?loc))
        :effect (and (not (in ?obj ?loc)) (not (armempty)) (holding ?obj))
)

(:action putdown
        :parameters (?obj - package ?loc - room)
        :precondition (and (rloc ?loc) (holding ?obj) (in ?obj ?loc))
        :effect (and (not (holding ?obj)) (armempty) (in ?obj ?loc))
)

(:action move
        :parameters (?d - door ?loc1 - room ?loc2 - room)
        :precondition (and (rloc ?loc1) (door ?loc1 ?loc2 ?d) (not (closed ?d)))
        :effect (and (rloc ?loc2) (not (rloc ?loc1)))
)

(:action open
        :parameters (?d - door ?loc1 - room ?loc2 - room)
        :precondition (and (rloc ?loc1) (door ?loc1 ?loc2 ?d) (closed ?d))
        :effect (and (not (closed ?d)))
)

(:method putdown_package_in_other_room
        :parameters (?obj - package ?loc1 - room ?loc2 - room ?d - door)
        :subgoals (and
        (task0 (go_to_room_with_package ?obj ?loc1 ?loc2 ?d))
        (task1 (putdown ?obj ?loc2))
        )
        :ordering (and
        (init < task0)
        (task0 < task1)
        (task1 < goal)
        )
)

(:method go_to_room_with_package
        :parameters (?obj - package ?loc1 - room ?loc2 - room ?d - door)
        :subgoals (and
        (task0 (pickup ?obj ?loc1))
        (task1 (open ?d ?loc1 ?loc2))
        (task2 (move ?d ?loc1 ?loc2))
        )
        :ordering (and
        (init < task0)
        (task0 < task1)
        (task1 < task2)
        (task2 < goal)
        )
)
)
