(define (problem BLOCKS-4-0)
(:domain BLOCKS)
(:objects D B A C - block)
(:init (clear C) (clear A) (clear B) (clear D) (ontable C) (ontable A)
 (ontable B) (ontable D) (handempty))
(:goal (AND (ON D C) (ON C B) (ON B A)))
)
