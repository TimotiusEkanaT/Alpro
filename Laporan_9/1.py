def bedafile(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            max_lines = max(len(lines1), len(lines2))
            differences_found = False

            for i in range(max_lines):
                line1 = lines1[i].strip() if i < len(lines1) else ""
                line2 = lines2[i].strip() if i < len(lines2) else ""
                words1 = line1.split()
                words2 = line2.split()
                different_words1 = []
                different_words2 = []
                max_words = max(len(words1), len(words2))
                for j in range(max_words):
                    w1 = words1[j] if j < len(words1) else "kosong"
                    w2 = words2[j] if j < len(words2) else "kosong"
                    if w1.lower() != w2.lower():
                        different_words1.append(w1)
                        different_words2.append(w2)
                if different_words1 or different_words2:
                    differences_found = True
                    print(f"\nPerbedaan pada baris {i+1}:")
                    print(f"File 1: {line1} | Perbedaan terdapat pada kata {', '.join(different_words1)}")
                    print(f"File 2: {line2} | Perbedaan terdapat pada kata {', '.join(different_words2)}")
            if not differences_found:
                print("Tidak ada perbedaan antara kedua file.")
    except FileNotFoundError as e:
        print("File tidak ditemukan:", e)

bedafile('file1.txt', 'file2.txt')