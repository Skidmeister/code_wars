# In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

# The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

# All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

# The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

# Have fun!

class Ribosome:
	"""class representing an object which will read the picks of the array"""
	def __init__(self):
		pass

	def count_picks(self, arr):
		positions = []
		picks = []
		plateau = "off"

		for x in range(len(arr)-2):
			self.pos_1 = arr[0+x]
			self.pos_2 = arr[1+x]
			self.pos_3 = arr[2+x]
			
			if plateau == "off":
				if self.pos_1 < self.pos_2:
					if self.pos_2 > self.pos_3:
						positions.append(x+1)
						picks.append(self.pos_2)
					elif self.pos_2 < self.pos_3:
						continue
					elif self.pos_2 == self.pos_3:
						plateau ="on"
						plat_1_value = self.pos_2
						plat_1_pos = x+1

			elif plateau == "on":
				if self.pos_2 > self.pos_3:
					positions.append(plat_1_pos)
					picks.append(plat_1_value)
					plateau = "off"
				elif self.pos_2 < self.pos_3:
					plateau = "off"
				elif self.pos_2 == self.pos_3:
					continue
		d = {"pos": positions, "peaks": picks}
		return d

def pick_peaks(arr):

	ribosome = Ribosome()

	return ribosome.count_picks(arr)