inputBahasa = input()

if inputBahasa == "PAS":
    print("""var data:array[1..10000] of longint;
    n,i,j,temp:longint;
begin
  readln(n);
  for i:=1 to n do readln(data[i]);
  for i:=1 to n-1 do
    for j:=i+1 to n do
      if (data[i]>data[j]) then
      begin
        temp:=data[i];
        data[i]:=data[j];
        data[j]:=temp;
      end;
  for i:=1 to n do writeln(data[i]);
end.""")
elif inputBahasa == "CPP":
    print("""int data[10001];
int n,i,j,temp;
int main(){
  scanf("%d",&n);
  for (i=1;i<=n;i++) scanf("%d",data[i]);
  for (i=1;i<=n-1;i++)
    for (j=i+1;j<=n;j++)
      if (data[i]>data[j]){
        temp=data[i];
        data[i]=data[j];
        data[j]=temp;
      }
  for (i=1;i<=n;i++) printf("%d\\n",data[i]);
  return 0;
}""")
