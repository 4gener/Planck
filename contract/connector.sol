pragma solidity 0.4.25; //it's different from asigeng;

contract YMHC{
    function name() public returns (string){};
}

contract Connector {
    YMHC instance;

    address owner = 0xD7d89224F239Af5999CF6C8f50a368A0Fe5Cec92;
    
    function Connector() public {
        
//        owner = msg.sender;
        // 从 `address` 到 `TokenCreator` ，是做显式的类型转换
        // 并且假定调用合约的类型是 TokenCreator，没有真正的方法来检查这一点。
        instance = YMHC(owner);
        
    }
    
    function get() public view returns(string result){
        return instance.name();
    }

//    function Value() external returns(ufixed propation){
        
//    }
    
    function Buy(address _from , uint256 _value) returns (bool success){
        
    }
}