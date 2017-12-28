package main


import (
	"github.com/parnurzeal/gorequest"
	"fmt"

	"encoding/json"


)

type GetblockhashRequest struct {
	Method     string `json:"method"`
	Params   []int  `json:"params"`
    Id         string `json:"id"`
}

type GetblockhashResult struct {
	Result string `json:"result"`
	Error string  `json:"error"`
	Id string `json:"id"`

}
type GetblockRequest struct{
	Method     string `json:"method"`
	Params   []string  `json:"params"`
	Id       string     `json:"id"`
}

type Getblock struct {
	Hash          string        `json:"hash"`
	Confirmations uint64        `json:"confirmations"`
	StrippedSize  int32         `json:"strippedsize"`
	Size          int32         `json:"size"`
	Weight        int32         `json:"weight"`
	Height        int64         `json:"height"`
	Version       int32         `json:"version"`
	VersionHex    string        `json:"versionHex"`
	MerkleRoot    string        `json:"merkleroot"`
	Tx            []string      `json:"tx,omitempty"`
	Time          int64         `json:"time"`
	Mediantime    int64         `json:"time"`
	Nonce         uint32        `json:"nonce"`
	Bits          string        `json:"bits"`
	Difficulty    float64       `json:"difficulty"`
	Previousblockhash  string        `json:"previousblockhash"`
	Nextblockhash      string        `json:"nextblockhash,omitempty"`
}

type GetblockResult struct {
	Result Getblock `json:"result"`
	Error string  `json:"error"`
	Id string `json:"id"`
}


func getblock(request gorequest.SuperAgent,blockhashs chan string,txids chan string,signal chan int){
OuterLoop:
	for {
		GetblockRequestArray :=[]GetblockRequest{}
		if len(blockhashs) >500{

			for i:=0;i<500;i++{
				blockhash := <-blockhashs
				gbrequest := GetblockRequest{"getblock", []string{blockhash}, "jsonrpc"}
				//gbrequestj, _ := json.Marshal(gbrequest)
				GetblockRequestArray=	append(GetblockRequestArray, gbrequest)


			}

		}else if len(blockhashs)>0{
			for i:=0;i<len(blockhashs);i++{

				blockhash := <-blockhashs
				gbrequest := GetblockRequest{"getblock", []string{blockhash}, "jsonrpc"}
				//gbrequestj, _ := json.Marshal(gbrequest)
				GetblockRequestArray=	append(GetblockRequestArray, gbrequest)

			}

		}else{
			signal <-1
			break OuterLoop
		}




		//getblock
		GetblockRequestArrayj,_:=json.Marshal(GetblockRequestArray)

		resp1, _, err := request.Post("http://127.0.0.1:8332").Send(string(GetblockRequestArrayj)).End()
		if err!= nil{
			fmt.Println(err)
		}
	//	fmt.Println(resp1.Body)
		gbresultArray := []GetblockResult{}
		json.NewDecoder(resp1.Body).Decode(&gbresultArray)
	//	fmt.Println(gbresult.Result.Tx)

		for i:=0;i<len(gbresultArray) ;i++{

			txs := gbresultArray[i].Result.Tx
			fmt.Println(gbresultArray[i].Result.Height,gbresultArray[i].Result.Hash,len(txs))
			for j := 0; j < len(txs); j++ {
		//					fmt.Println(gbresultArray[i].Result.Hash,":",txs[j])
				txids <- txs[j]
			}

		}



	}
}
func getblockhash(request gorequest.SuperAgent, heights chan int,blockhashs chan string,signal chan int){
	OuterLoop:
	for {

		GetblockhashRequestArray :=[]GetblockhashRequest{}
		if len(heights) >500{

			for i:=0;i<500;i++{
				height := <-heights
				gbhrequest := GetblockhashRequest{"getblockhash", []int{height}, "jsonrpc"}
				//gbrequestj, _ := json.Marshal(gbrequest)
				GetblockhashRequestArray=	append(GetblockhashRequestArray, gbhrequest)


			}

		}else if len(heights)>0{
			for i:=0;i<len(heights);i++{

				height := <-heights
				gbhrequest := GetblockhashRequest{"getblockhash", []int{height}, "jsonrpc"}
				//gbrequestj, _ := json.Marshal(gbrequest)
				GetblockhashRequestArray=	append(GetblockhashRequestArray, gbhrequest)

			}

		}else{
			signal <-1
			fmt.Println("getblockhash finished")
			break OuterLoop
		}







		//getblockhash

		GetblockhashRequestArrayj, _ := json.Marshal(GetblockhashRequestArray)

		resp, _, err := request.Post("http://127.0.0.1:8332").Send(string(GetblockhashRequestArrayj)).End()
		if err!= nil{
			fmt.Println(err)
		}
	//	fmt.Println(resp.Body)
		gbhresultArray := []GetblockhashResult{}
		json.NewDecoder(resp.Body).Decode(&gbhresultArray)
	//	fmt.Println(len(gbhresultArray))
	for i:=0;i<len(gbhresultArray);i++{
		fmt.Println(gbhresultArray[i].Result)
		blockhashs <-gbhresultArray[i].Result
	}





	}

}


func main(){

 //  totalheight:= int(10)  //10 0..9 getblockhash 9 000000008d9dc510f23c2657fc4f67bea30078cc05a90eb89e84cc475c080805
	totalheight:= int(501289) // 501289 0..501289 getblockhash 501289  0000000000000000003a713555385e99bb70398007da8a763cc039cf11594d37
	request := gorequest.New().SetBasicAuth("admin", "admin").
		Set("content_type","application/json")

    signal := make(chan int,2)
	heights := make(chan int,totalheight)
	blockhashs :=make(chan string,totalheight)
	txids:=make(chan string,300000000)

	for i:=0;i<totalheight;i++{
        heights <- int(i)

	}



		go getblockhash(*request,heights,blockhashs,signal)
	<-signal
		go getblock(*request,blockhashs,txids,signal)

	<-signal



	//db, err := leveldb.OpenFile("D:\\heighttest", nil)
	//
	//if err != nil{
	//	fmt.Println(err)
	//}
	//defer db.Close()












//		bb:=[]string{}

//for j:=0;j < 200000000;j=j+5000 {
//
//	fmt.Println(j)
//	for i := j; i < j+5000; i++ {
//
//	//	fmt.Println(i)
//		getblockhash := Getblockhash{"getblockhash", []int{i},"jsonrpc"}
//		b, err := json.Marshal(getblockhash)
//		if err != nil {
//			fmt.Println("error:", err)
//		}
//		bb = append(bb, string(b))
//
//	}
//	//fmt.Println(strings.Join(bb, ","))
//
//	resp, _, errs := request.Post("http://127.0.0.1:8332").
//		Send("[" + strings.Join(bb, ",") + "]").End()
//
//	if errs != nil {
//		fmt.Println(errs)
//
//	}
//	fmt.Println(resp.Body)
//
//}

}