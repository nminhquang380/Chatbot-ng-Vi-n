import fasttext

model = fasttext.train_supervised(input="data_train_final.txt", wordNgrams=2)

model.save_model("model_dangvien.bin")

model = fasttext.load_model("model_dangvien.bin")

def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))

print_results(*model.test('dangvien_test_pre.txt'))