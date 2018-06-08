int i=0;
    int A_size=A.size();
    int count=0;
    while(i<=A_size/2)
    {
        
        if(i>=count&&A[i]>=count){
            // cout<<A[i]<<" and 1 "<<A[A[i]]<<"\n";
            int f=-1;
            if(i==0)
            {
                f = A[A[A[i]]];
                // cout<<"\nF:"<<f;
            }
            int t=A[i];
            A[i]=A[A[i]];
            A[A[i]]=t;
            if(f!=-1)
            {
                A[A[A[i]]]=f;
            }
        }
        else{
            // cout<<A[i]<<" and "<<A[A[A[i]]]<<"\n";
            int t=A[i];
            // cout<<"\nT:"<<t;
            A[i]=A[A[A[i]]];
            // cout<<"\nA[i]:"<<A[i];
            A[A[t]]=t;
            // cout<<A[i]<<" and "<<A[A[A[i]]]<<"\n";
        }
        // if(A[i]==i)
        // cout<<"\n";
        //     for(int j=0;j<A_size;j++)
        //     cout<<A[j]<<" ";
        //     cout<<"\n";
        count++;
            i++;
    }