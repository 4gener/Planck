pragma solidity 0.4.25; //it's different from asigeng;

contract YMHC{
    mapping (address => uint256) public balanceOf;
    function nbTransfer(address _from, address _to, uint256 _value) public returns (bool success){}
    function getBalance(address _add) public returns (uint256 value){}
    function setBalance(address _add, uint256 _value) public returns (bool success) {}
}

contract vETHConnector{
//    function vETHConnector() public{}
    function getValue() external returns(uint256 propation){}
    function buySmartToken(address _from , uint256 _value) returns (uint256 value){}
    function buyVETH (address _from , uint256 _value) returns (uint256 value){}
}

contract aETHConnector{
//    function aETHConnector() public{}
    function getValue() external returns(uint256 propation){}
    function buySmartToken(address _from , uint256 _value) returns (uint256 value){}
    function buyAETH (address _from , uint256 _value) returns (uint256 value){}
}

contract Adaptor{
    aETHConnector aETH;
    vETHConnector vETH;
    
    address vAddress = 0x72673e92ae4033682321705342785919676DcD3B;
    address aAddress = 0x3B6082940394D8150a6229A9FFDea9417785E32c;
    
    function Adaptor() public {
        aETH = aETHConnector(aAddress);
        vETH = vETHConnector(vAddress);
    }
    
    function aETH_To_vETH(address _from , uint256 _value){
       uint256 result = aETH.buySmartToken(_from , _value);
       vETH.buyVETH(_from , _value);
    }
    
    function vETH_To_aETH(address _from , uint256 _value){
       uint256 result = vETH.buySmartToken(_from , _value);
       aETH.buyAETH(_from , _value);
    }
    
}