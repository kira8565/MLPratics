from recoments.recommendations import critics, sim_distance, sim_pearson

print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
