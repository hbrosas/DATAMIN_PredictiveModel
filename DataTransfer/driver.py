import csv

class Driver:

	def writeToCSV(data):
		final_data = []
		header = ["month", "day", "year", "start_time", "end_time", 
				"north_avenue_entry", 	"north_avenue_exit", 
				"quezon_avenue_entry", 	"quezon_avenue_exit",
				"gma_kamuning_entry", 	"gma_kamuning_exit",
				"cubao_entry", 		"cubao_exit",
				"santolan_entry", 		"santolan_exit",
				"ortigas_entry", 		"ortigas_exit", 
				"shaw_blvd_entry", 		"shaw_blvd_exit",
				"boni_avenue_entry", 	"boni_avenue_exit",
				"guadalupe_entry", 		"guadalupe_exit",
				"buendia_entry", 		"buendia_exit",
				"ayala_avenue_entry", 	"ayala_avenue_exit",
				"magallanes_entry", 	"magallanes_exit",
				"taft_entry", 			"taft_exit" ]

		file_writer = csv.writer(open('../Data/edited/2014.csv', 'w+', newline=''), delimiter=',')
		print("File Successfully Created!")

		for d in data:
			row_data = []
			row_data.append(d[0])
			row_data.append(d[1])
			row_data.append("2014")
			timeslot = d[2].split("-")
			row_data.append(timeslot[0])
			row_data.append(timeslot[1])

			for x in range(3, 29):
				row_data.append(d[x])

			final_data.append(row_data)

		file_writer.writerows(final_data)
		print("Transferring Done!")

	def init():
		data = []
		isHeader = True
		
		file_reader = csv.reader(open('../Data/2014.csv', 'rt', encoding="UTF8"), delimiter=',')
		print("File Successfully Read!")
		for row in file_reader:
			if isHeader:
				# Get header
				isHeader = False
			else:
				# Add to data
				data.append(row)

		return data

	data = init()
	writeToCSV(data)