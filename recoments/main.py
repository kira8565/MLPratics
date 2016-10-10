from recoments.recommendations import critics, sim_distance, sim_pearson, topMatches, getRecommendations
import pydelicious
print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
print(topMatches(critics, 'Toby', n=3))
print(getRecommendations(critics, 'Toby'))
