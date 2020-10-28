from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
import dev52
import dev53


def calculate_scores(x_true, x_pred):  # [正解, 予想] 正解率予想関数

    # 適合率
    precision = precision_score(x_true, x_pred, average=None, labels=['b', 'e', 't', 'm'])
    precision = np.append(precision, precision_score(x_true, x_pred, average='micro'))
    precision = np.append(precision, precision_score(x_true, x_pred, average='macro'))

    # 再現率
    recall = recall_score(x_true, x_pred, average=None, labels=['b', 'e', 't', 'm'])
    recall = np.append(recall, recall_score(x_true, x_pred, average='micro'))
    recall = np.append(recall, recall_score(x_true, x_pred, average='macro'))

    # F1スコア
    f1 = f1_score(x_true, x_pred, average=None, labels=['b', 'e', 't', 'm'])
    f1 = np.append(f1, f1_score(x_true, x_pred, average='micro'))
    f1 = np.append(f1, f1_score(x_true, x_pred, average='macro'))

    # 結果をデータフレームにして見やすくする
    score = pd.DataFrame({'適合率': precision, '再現率': recall, 'F1スコア': f1},
                         index=['b', 'e', 't', 'm', 'マイクロ平均', 'ミクロ平均'])
    return score


def main():
    data = dev52.Lg()
    feature_test = data[2][0]
    test_category = data[2][1]
    test_pred = dev53.pred(feature_test, test_category)
    print(calculate_scores(test_category, test_pred))


if __name__ == '__main__':
    main()
