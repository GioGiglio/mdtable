# MDTable
## Description
Reads from the stdin a space separated text, and prints on the stdout the markdown syntaxt of a table made by the text readed.

## Usage
- `$ whatever | ./mdtable COLNAME_1 COLNAME_2 ... COLNAME_N` Creates a table with the specified column names, starting by the output of `whatever`

- `$ whatever | ./mdtable -f` Creates a table and uses the content of the first line of the output of`whatever` as the column names.

Make sure to give __execution permission__ to the script so that it can be executed via `./mdtable.py`

### Example
Let's assume that you want to create a table of the current processes in your machine. <br>
These are the first lines of output of the `ps -aux` command:

```bash
$ ps -aux | head
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 120016  6188 ?        Ss   21:38   0:02 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S    21:38   0:00 [kthreadd]
root         6  0.0  0.0      0     0 ?        S    21:38   0:00 [ksoftirqd/0]
root         7  0.4  0.0      0     0 ?        S    21:38   0:22 [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    21:38   0:00 [rcu_bh]
root         9  0.0  0.0      0     0 ?        S    21:38   0:00 [migration/0]
root        10  0.0  0.0      0     0 ?        S<   21:38   0:00 [lru-add-drain]
root        11  0.0  0.0      0     0 ?        S    21:38   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    21:38   0:00 [cpuhp/0]
```
To create a table, just __pipe__ the output to the `mdtable.py` script, and use `-f` flag to use the first line as the table headers.

```bash
$ ps -aux | head | ./mdtable -f
USER | PID | %CPU | %MEM | VSZ | RSS | TTY | STAT | START | TIME | COMMAND
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
root | 1 | 0.0 | 0.0 | 120016 | 6188 | ? | Ss | 21:38 | 0:02 | /sbin/init splash
root | 2 | 0.0 | 0.0 | 0 | 0 | ? | S | 21:38 | 0:00 | [kthreadd]
root | 6 | 0.0 | 0.0 | 0 | 0 | ? | S | 21:38 | 0:00 | [ksoftirqd/0]
root | 7 | 0.4 | 0.0 | 0 | 0 | ? | S | 21:38 | 0:24 | [rcu_sched]
root | 8 | 0.0 | 0.0 | 0 | 0 | ? | S | 21:38 | 0:00 | [rcu_bh]
root | 9 | 0.0 | 0.0 | 0 | 0 | ? | S | 21:38 | 0:00 | [migration/0]
root | 10 | 0.0 | 0.0 | 0 | 0 | ? | S< | 21:38 | 0:00 | [lru-add-drain]
root | 11 | 0.0 | 0.0 | 0 | 0 | ? | S | 21:38 | 0:00 | [watchdog/0]
root | 12 | 0.0 | 0.0 | 0 | 0 | ? | S | 21:38 | 0:00 | [cpuhp/0]
```
Now you can redirect this output to a __markdown__ file and create an HTML from it that will result in something like this table below.

<table>
<thead>
<tr>
<th>USER</th>
<th>PID</th>
<th>%CPU</th>
<th>%MEM</th>
<th>VSZ</th>
<th>RSS</th>
<th>TTY</th>
<th>STAT</th>
<th>START</th>
<th>TIME</th>
<th>COMMAND</th>
</tr>
</thead>
<tbody>
<tr>
<td>root</td>
<td>1</td>
<td>0.0</td>
<td>0.0</td>
<td>120016</td>
<td>6188</td>
<td>?</td>
<td>Ss</td>
<td>21:38</td>
<td>0:02</td>
<td>/sbin/init splash</td>
</tr>
<tr>
<td>root</td>
<td>2</td>
<td>0.0</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S</td>
<td>21:38</td>
<td>0:00</td>
<td>[kthreadd]</td>
</tr>
<tr>
<td>root</td>
<td>6</td>
<td>0.0</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S</td>
<td>21:38</td>
<td>0:00</td>
<td>[ksoftirqd/0]</td>
</tr>
<tr>
<td>root</td>
<td>7</td>
<td>0.4</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S</td>
<td>21:38</td>
<td>0:25</td>
<td>[rcu_sched]</td>
</tr>
<tr>
<td>root</td>
<td>8</td>
<td>0.0</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S</td>
<td>21:38</td>
<td>0:00</td>
<td>[rcu_bh]</td>
</tr>
<tr>
<td>root</td>
<td>9</td>
<td>0.0</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S</td>
<td>21:38</td>
<td>0:00</td>
<td>[migration/0]</td>
</tr>
<tr>
<td>root</td>
<td>10</td>
<td>0.0</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S&lt;</td>
<td>21:38</td>
<td>0:00</td>
<td>[lru-add-drain]</td>
</tr>
<tr>
<td>root</td>
<td>11</td>
<td>0.0</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S</td>
<td>21:38</td>
<td>0:00</td>
<td>[watchdog/0]</td>
</tr>
<tr>
<td>root</td>
<td>12</td>
<td>0.0</td>
<td>0.0</td>
<td>0</td>
<td>0</td>
<td>?</td>
<td>S</td>
<td>21:38</td>
<td>0:00</td>
<td>[cpuhp/0]</td>
</tr>
</tbody>
</table>
