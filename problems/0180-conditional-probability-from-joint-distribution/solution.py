def conditional_probability(joint_distribution: dict) -> float:
	return joint_distribution[('A','B')]/(joint_distribution[('A','B')] + joint_distribution[('`A','B')]) 