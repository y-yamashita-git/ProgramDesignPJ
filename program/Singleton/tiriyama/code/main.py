from TiriyamaComputer import TiriyamaComputer

if __name__ == "__main__":
    #クラスインスタンス化
    tiriyama_cp_001 = TiriyamaComputer()
    tiriyama_cp_002 = TiriyamaComputer()
    
    # インスタンスが同じかチェック
    if tiriyama_cp_001 is tiriyama_cp_002:
        print("inctance check : Same instance  [ {} == {} ]".format(tiriyama_cp_001.get_instance(), tiriyama_cp_002.get_instance()))
    else:
        print("inctance check : Different instance  [ {} == {} ]".format(tiriyama_cp_001.get_instance(), tiriyama_cp_002.get_instance()))
    
    # インスタンス内のmacアドレスを取得
    tiriyama_cp_mac_address = tiriyama_cp_001.get_mac_address()
    print(tiriyama_cp_mac_address)
